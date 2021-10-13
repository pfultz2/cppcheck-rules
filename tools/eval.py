import re, sys

def block():
    return '({[^{}]*(?-1)*[^{}]*})'

def paren():
    return '(\\([^()]*(?-1)*[^()]*\\))'

def name():
    return '(?:\\w+ :: )*\\w+'

def type():
    return '(?:(?:\\w+|<|>|::) )*(?:\\w+|>)(?: &|\\*)*'

def stmt():
    wildcard = '[^{}]*'
    return '(?:{wildcard}{block}{wildcard})*?'.format(wildcard=wildcard, block=block())

def until_paren():
    wildcard1 = '[^()]*'
    wildcard2 = '[^)]*\\)'
    return '(?:{wildcard1}{paren})*{wildcard2}'.format(wildcard1=wildcard1, wildcard2=wildcard2, paren=paren())

def until_semi():
    return '[^;]*;'

symbols = {
    '[': '\\[',
    '[[': '[',
    ']': '\\]',
    ']]': ']',
    '(': '\\(',
    '((': '(',
    ')': '\\)',
    '))': ')',
    '++': '\\+\\+',
    '--': '\\-\\-',
    '?': '\\?',
    '*;': until_semi(),
    '*)': until_paren(),
    '{*}': block(),
    '(*)': paren(),
    '$stmt': stmt(),
    '$name': name(),
    '$type': type()
}

prefix = [
    '(?:',
    '(?>',
    '(?|',
    '('
]

suffix = [
    ')?',
    ')',
    '*',
    '+'
]

def q_word(word):
    if word in symbols:
        return symbols[word]
    elif word.startswith('(?<'):
        idx = word.find('>')
        return word[0:idx+1]+q_word(word[idx+1:])
    for x in prefix:
        if word.startswith(x) and word != x:
            return x+q_word(word[len(x):])
    for x in suffix:
        if word.endswith(x) and word != x:
            return q_word(word[0:-len(x)])+x
    if word.startswith('$'):
        return '\\'+word[1:]
    return word

def q_words(s):
    words = s.split()
    skip = False
    for word in words:
        if word == '<%':
            skip = True
        if skip:
            if word == '%>':
                skip = False
            yield word
        elif '|' in word and not word.startswith('|'):
            yield '|'.join([q_word(x) for x in word.split('|')])
        else:
            yield q_word(word)

def q(s):
    return ' '.join(q_words(s))

def for_idx_loop(inner):
    return q("for ( $type ($w+) = $w+ ; $1 < $w+ ; ($1 ++|++ $1|$1 --|-- $1) ) {{ {} }}").format(inner)

def for_range_loop(inner):
    # return q("for ( $type ($w+) : ([^()]+) ) {{ {} }}").format(inner)
    return q("for ( $type ($w+) : *) {{ {} }}").format(inner)

def template_eval(template, **kwargs):
    start = '<%'
    end = '%>'
    escaped = (re.escape(start), re.escape(end))
    mark = re.compile('%s(.*?)%s' % escaped, re.DOTALL)
    for key in kwargs:
        exec('%s = %s' % (key, kwargs[key]))
    for item in mark.findall(template):
        template = template.replace(start+item+end, str(eval(item.strip())))
    return template

def cdata(s):
    return "<![CDATA[{}]]>".format(s)

def regex_eval(template):
    start = '<['
    end = ']>'
    escaped = (re.escape(start), re.escape(end))
    mark = re.compile('%s(.*?)%s' % escaped, re.DOTALL)
    for item in mark.findall(template):
        template = template.replace(start+item+end, cdata(q(item.strip())))
    return template

f = open(sys.argv[1]).read()
r = template_eval(regex_eval(f))
sys.stdout.write(r)

import re, sys

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
    '--': '\\-\\-'
}

def q_word(word):
    if word in symbols:
        return symbols[word]
    elif word.startswith('(') and word != '(':
        return '('+q_word(word[1:])
    elif word.endswith(')') and word != ')':
        return q_word(word[0:-1])+')'
    elif word.startswith('$'):
        return '\\'+word[1:]
    else:
        return word

def q_words(s):
    words = s.split()
    for word in words:
        if '|' in word and not word.startswith('|'):
            yield '|'.join([q_word(x) for x in word.split('|')])
        else:
            yield q_word(word)

def q(s):
    return ' '.join(q_words(s))


def block():
    return '({[^{}]*(?1)*[^{}]*})'

def paren():
    return "\\( [^()]+ \\)"

def for_idx_loop(inner):
    # return "for \\( \\w+ (\\w+) = \\w+ ; \\1 < \\w+ ; (\\1 \\+\\+|\\+\\+ \\1|\\1 \\-\\-|\\-\\- \\1) \\) {{ {} }}".format(inner)
    return q("for ( $w+ ($w+) = $w+ ; $1 < $w+ ; ($1 ++|++ $1|$1 --|-- $1) ) {{ {} }}").format(inner)

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

f = open(sys.argv[1]).read()
r = template_eval(f)
sys.stdout.write(r)

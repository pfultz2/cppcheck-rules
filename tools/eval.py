import re, sys

def block():
    return '({[^{}]*(?1)*[^{}]*})'

def paren():
    return "\\( [^()]+ \\)"

def for_idx_loop(inner):
    return "for \\( \\w+ (\\w+) = \\w+ ; \\1 < \\w+ ; (\\1 \\+\\+|\\+\\+ \\1|\\1 \\-\\-|\\-\\- \\1) \\) {{ {} }}".format(inner)

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

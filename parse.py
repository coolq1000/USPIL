import re

class Parser:

    def __init__(self, code):
        self.code = code
        self.assemble = []

    def repl(self, a):
        op = a.group(0).split(', ')
        op = '[' + ', '.join([(x.upper() if i == 0 else x) for i, x in enumerate(op) if x not in ['"("', '")"']]) + ']'
        return op

    def parse(self):
        t = []
        v = []
        for token in self.code:
            t += [token.name]
            v += [token.value]
        
        todo = (', '.join([('"' + str(x) + '"' if x is not '{' and x is not '}' else str(x)) for x in v]).replace('{', '[').replace('}', ']').replace('[,', '[').replace(', ]', ']'))
        todo = re.sub(r'".*?", "\(", (".*?",) "\)"', self.repl, todo)
        exec('self.assemble = [' + todo + ']')
        return self.assemble


class Language:

    def __init__(self, code):
        self.code = code
        self.lines = [0]
        self.stack = []
        self.variables = {}
    
    def evaluate(self, parts):
        for i, part in enumerate(parts):
            if part in self.variables:
                parts[i] = self.variables[part]
        e = ' '.join([str(part) for part in parts])
        return eval(e)
    
    def is_block(self):
        if type(self.get()[0]) is list:
            return True
        return False

    def get(self, parent=False):
        c = self.code[:]
        l = self.lines[:]
        while len(l) > parent:
            c = c[l.pop(0)]
        return c
    
    def cycle(self):
        while self.lines[0] < len(self.code):
            if self.lines[-1] >= len(self.get(parent=True)):
                self.lines.pop()
                if len(self.lines) > 0 and len(self.stack) > 0 and len(self.lines) == self.stack[-1]:
                    self.lines[-1] -= 1
                    self.stack.pop()
                else:
                    self.lines[-1] += 1
                    continue
            while self.is_block():
                self.lines += [0]
            
            line = self.get()
            op = line[0]
            args = line[1:]

            if   op == 'IF':
                if not self.evaluate(args):
                    self.lines[-1] += 1
            
            elif op == 'PRINT':
                print(self.evaluate(args))
            
            elif op == 'WHILE':
                if not self.evaluate(args):
                    self.lines[-1] += 1
                else:
                    self.stack += [len(self.lines)]
            elif op == 'VAR':
                self.variables[args[0]] = self.evaluate(args[2:])
            elif op == 'COMMENT':
                pass
            self.lines[-1] += 1

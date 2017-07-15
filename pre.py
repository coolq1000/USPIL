import re, sys, os

class PreProcessor:

    def __init__(self, code):
        self.code = code
    
    def require_file(self, a):
        prog = a.group(1)
        if os.path.exists(prog):
            with open(a.group(1)[1:-1]) as f:
                return f.read()
        else:
            try:
                with open(a.group(1)[1:-1] + '.prog') as f:
                    return f.read()
            except FileNotFoundError:
                print('ERROR: Couldn\'t find library {}.'.format(a.group(1)))
                sys.exit(1)
        return ''

    def parse(self):
        while len(re.findall(r'require\s*?\((.*?)\)', self.code)) > 0:
            self.code = re.sub(r'require\s*?\((.*?)\)', self.require_file, self.code)
        return self.code

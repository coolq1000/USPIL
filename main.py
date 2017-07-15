from interpreter import *
from parse       import *
from lexer       import *
from pre         import *
import sys

if len(sys.argv) > 1:
    with open(sys.argv[1], 'r') as f:
        code = f.read()
else:
    print('ERROR: Expected file.')
    sys.exit(1)

prep = PreProcessor(code)
code = prep.parse()
lexer = Lexer(code)
code = lexer.lex()
parser = Parser(code)
code = parser.parse()
lang = Language(code)
lang.cycle()

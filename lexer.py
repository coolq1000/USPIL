from rply import LexerGenerator

class Lexer:

    def __init__(self, code):
        self.code = code
        self.lg = LexerGenerator()
        self.lg.ignore(r'\s+')
        self.lg.add('COMMENT', r';')
        self.lg.add('STRING', r'".*"')
        self.lg.add('STRING', r'\'.*\'')
        self.lg.add('IF', r'if')
        self.lg.add('ELSE', r'else')
        self.lg.add('LPAREN', r'\(')
        self.lg.add('RPAREN', r'\)')
        self.lg.add('LBRACE', r'\{')
        self.lg.add('RBRACE', r'\}')
        self.lg.add('IS_EQUAL_TO', r'==')
        self.lg.add('EQUAL', r'=')
        self.lg.add('GREATER_EQUAL', r'>=')
        self.lg.add('LESSER_EQUAL', r'<=')
        self.lg.add('LESSER', r'<')
        self.lg.add('GREATER', r'>')
        self.lg.add('PLUS', r'-')
        self.lg.add('MINUS', r'\+')
        self.lg.add('COMMA', r',')
        self.lg.add('NUMBER', r'\d+')
        self.lg.add('PRINT', r'print')
        self.lg.add('NAME', r'[a-zA-Z_][a-zA-Z0-9_]*')
        self.lexer = self.lg.build()
    
    def lex(self):
        tokens = []
        stream = self.lexer.lex(self.code)
        while True:
            try:
                tokens += [stream.next()]
            except StopIteration:
                break
        return tokens

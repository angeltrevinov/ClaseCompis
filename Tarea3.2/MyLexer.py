import ply.lex as lex

class MyLexer(object):

    # Definition of tokens
    tokens = [
        'TWODOTS',
        'COMMA',
        'SEMICOLON',
        'OPENBRACKET',
        'CLOSEBRACKET',
        'EQUALS',
        'BIGGERTHAN',
        'SMALLTHAN',
        'DIFFERENTTHAN',
        'SUBTRACT',
        'SUM',
        'TIMES',
        'DIV',
        'OPENPAREN',
        'CLOSEPAREN',
        'ID',
        'CTEINT',
        'CTEFLOAT',
        'CTESTRING'
    ]

    # Definition of Reserved Words
    reserved = {
        'if'        :       'IF',
        'else'      :       'ELSE',
        'var'       :       'VAR',
        'print'     :       'PRINT',
        'program'   :       'PROGRAM',
        'int'       :       'INT',
        'float'     :       'FLOAT'
    }

    # Regular expresion rules for simple tokens
    t_TWODOTS           = r'\:'
    t_COMMA             = r'\,'
    t_SEMICOLON         = r'\;'
    t_OPENBRACKET       = r'\{'
    t_CLOSEBRACKET      = r'\}'
    t_EQUALS            = r'\='
    t_BIGGERTHAN        = r'\>'
    t_SMALLTHAN         = r'\<'
    t_DIFFERENTTHAN     = r'\<\>'
    t_SUBTRACT          = r'\-'
    t_SUM               = r'\+'
    t_TIMES             = r'\*'
    t_DIV               = r'\/'
    t_OPENPAREN         = r'\('
    t_CLOSEPAREN        = r'\)'
    t_ignore            = ' \t\n'

    def t_CTESTRING(self, t):
        r'\"(.*)\"'
        t.value = str(t.value)
        return t

    def t_CTEFLOAT(self, t):
        r'\d+\.\d+'
        t.value = float(t.value)
        return t

    def t_CTEINT(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_ID(self, t):
        r'[a-zA-Z_][a-zA-Z_0-9]*'
        t.type = self.reserved.get(t.value, 'ID')
        return t

    def t_error(self, t):
        print("\n Token no apropiado\n")
        t.lexer.skip(1)

    # constructor
    def __init__(self):
        # adding reserve to tokens list
        self.tokens += list(self.reserved.values())
        self.lexer = lex.lex(module=self)
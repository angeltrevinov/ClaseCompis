import ply.yacc as yacc
from MyLexer import *


class MyParser:
    __error = False
    tokens = MyLexer.tokens

    # Definition of grammatic rules
    def p_program(self, p):
        '''
        program : PROGRAM ID SEMICOLON vars bloque
                | PROGRAM ID SEMICOLON bloque
        '''
        pass

    def p_vars(self, p):
        '''
        vars : VAR vars2
        '''
        pass

    def p_vars2(self, p):
        '''
        vars2 : vars3 TWODOTS tipo SEMICOLON vars2
              | vars3 TWODOTS tipo SEMICOLON
        '''
        pass

    def p_vars3(self, p):
        '''
        vars3 : ID COMMA vars3
              | ID
        '''
        pass

    def p_tipo(self, p):
        '''
        tipo : INT
             | FLOAT
        '''
        pass

    def p_bloque(self, p):
        '''
        bloque : OPENBRACKET estatuto bloque1 CLOSEBRACKET
               | OPENBRACKET estatuto CLOSEBRACKET
               | OPENBRACKET CLOSEBRACKET
        '''
        pass

    def p_bloque1(self, p):
        '''
        bloque1 : estatuto bloque1
                | estatuto
        '''
        pass

    def p_estatuto(self, p):
        '''
        estatuto : asignacion
                 | condicion
                 | escritura
        '''
        pass

    def p_condicion(self, p):
        '''
        condicion : IF OPENPAREN expresion CLOSEPAREN bloque ELSE bloque SEMICOLON
                  | IF OPENPAREN expresion CLOSEPAREN bloque SEMICOLON
        '''
        pass

    def p_escritura(self, p):
        '''
        escritura : PRINT OPENPAREN es1 CLOSEPAREN SEMICOLON
        '''
        pass

    def p_es1(self, p):
        '''
        es1 : expresion
            | CTESTRING
            | expresion COMMA es1
            | CTESTRING COMMA es1
        '''
        pass

    def p_asignacion(self, p):
        '''
        asignacion : ID EQUALS expresion SEMICOLON
        '''
        pass

    def p_expresion(self, p):
        '''
        expresion : exp BIGGERTHAN exp
                  | exp SMALLTHAN exp
                  | exp DIFFERENTTHAN exp
                  | exp
        '''
        pass

    def p_exp(self, p):
        '''
        exp : termino exp1 exp
            | termino
        '''
        pass

    def p_exp1(self, p):
        '''
        exp1 : SUM
             | SUBTRACT
        '''
        pass

    def p_termino(self, p):
        '''
        termino : factor t1 termino
                | factor
        '''
        pass

    def p_t1(self, p):
        '''
        t1 : TIMES
            | DIV
        '''
        pass

    def p_factor(self, p):
        '''
        factor : OPENPAREN expresion CLOSEPAREN
               | SUM varcte
               | SUBTRACT varcte
               | varcte
        '''
        pass

    def p_varcte(self, p):
        '''
        varcte : ID
               | CTEINT
               | CTEFLOAT
        '''
        pass

    def p_error(self, p):
        self.__error = True
        print('\n gramatica no apropiada \n', p)

    # constructor
    def __init__(self, lexer):
        self.parser = yacc.yacc(module=self)
        self.lexer = lexer

    def get_error(self):
        return self.__error

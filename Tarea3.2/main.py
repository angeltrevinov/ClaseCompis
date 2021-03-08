# Press the green button in the gutter to run the script.
from MyLexer import *
from MyParser import *

if __name__ == '__main__':
    file_name = input('Ingresa el nombre del archivo: \n')
    file = open(file_name, 'r')
    src_file = file.read()

    my_lexer = MyLexer()
    my_pars = MyParser(my_lexer)

    lex = my_lexer.lexer
    parser = my_pars.parser

    result = parser.parse(src_file)
    if my_pars.get_error() != True :
        print("Se pudo parsear correctamente")

    file.close()


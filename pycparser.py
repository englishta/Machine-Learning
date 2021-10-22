import sys
from pycparser import parse_file, c_parser, c_generator, c_ast

def main():
    text = ''.join(sys.stdin.readlines()) # �ǂݍ���
    parser = c_parser.CParser() # �p�[�T
    ast = parser.parse(text, filename='<none>') # �p�[�X����
    ast.show()

if __name__ =='__main__':
    main()
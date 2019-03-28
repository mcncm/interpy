#! /bin/python

keywords = {
'Faux'           : 'False',
'Aucune'         : 'None',
'Vrai'           : 'True',
'et'             : 'and',
'comme'          : 'as',
'affirme'        : 'assert',
#                : 'async',
#                : 'await',
#                : 'break',
'classe'         : 'class',
#                : 'continue',
'déf'            : 'def',
'eff'            : 'del',
'sinonsi'        : 'elif',
'sinon'          : 'else',
#                : 'except',
'enfin'          : 'finally',
'pour'           : 'for',
'de'             : 'from',
#                : 'global',
'si'             : 'if',
'importe'        : 'import',
'dans'           : 'in',
'est'            : 'is',
#                : 'lambda',
#                : 'nonlocal',
'pas'            : 'not',
'ou'             : 'or',
'passe'          : 'pass',
#                : 'raise',
'remets'         : 'return',
'essaye'        : 'try',
'pendant'        : 'while',
'avec'           : 'with',
#                : 'yield'
}

functions = {
'imprime'       : 'print',
}

tokens = {}
tokens.update(keywords)
tokens.update(functions)

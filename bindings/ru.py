#! /bin/python

keywords = {
'Ложными'        : 'False',
#                : 'None',
'Истинными'      : 'True',
'и'              : 'and',
#                : 'as',
#                : 'assert',
#                : 'async',
#                : 'await',
#                : 'break',
'класс'          : 'class',
#                : 'continue',
'опр'            : 'def',
#                : 'del',
#                : 'elif',
#                : 'else',
#                : 'except',
#                : 'finally',
#                : 'for',
#                : 'from',
#                : 'global',
'если'           : 'if',
#                : 'import',
'в'              : 'in',
#                : 'is',
#                : 'lambda',
#                : 'nonlocal',
'не'             : 'not',
'или'            : 'or',
#                : 'pass',
#                : 'raise',
#                : 'return',
#                : 'try',
#                : 'while',
'с'              : 'with',
#                : 'yield'
}

functions = {
'распечатай'       : 'print',
}

tokens = {}
tokens.update(keywords)
tokens.update(functions)

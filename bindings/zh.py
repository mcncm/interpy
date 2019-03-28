#! /bin/python

keywords = {
'假'             : 'False',
#                : 'None',
'真'             : 'True',
'和'             : 'and',
#                : 'as',
#                : 'assert',
#                : 'async',
#                : 'await',
#                : 'break',
'类'             : 'class',
#                : 'continue',
'定'             : 'def',
#                : 'del',
#                : 'elif',
#                : 'else',
#                : 'except',
#                : 'finally',
#                : 'for',
#                : 'from',
#                : 'global',
'如'             : 'if',
#                : 'import',
'在'             : 'in',
'是'             : 'is',
#                : 'lambda',
#                : 'nonlocal',
'不'             : 'not',
'或'             : 'or',
#                : 'pass',
#                : 'raise',
#                : 'return',
#                : 'try',
#                : 'while',
'同'             : 'with',
#                : 'yield'
}

functions = {
'印'       : 'print',
}

tokens = {}
tokens.update(keywords)
tokens.update(functions)

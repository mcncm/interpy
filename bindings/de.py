#! /bin/python

keywords = {
'Falsch'         : 'False',
'Kein'           : 'None',
'Wahr'           : 'True',
'und'            : 'and',
'als'            : 'as',
#                : 'assert',
#                : 'async',
#                : 'await',
#                : 'break',
'klasse'         : 'class',
#                : 'continue',
#                : 'def',
#                : 'del',
#                : 'elif',
#                : 'else',
#                : 'except',
'endlich'        : 'finally',
'fuer'           : 'for',
'aus'            : 'from',
#                : 'global',
'wenn'           : 'if',
#                : 'import',
#                : 'in",
'ist'            : 'is',
#                : 'lambda',
#                : 'nonlocal',
'nicht'          : 'not',
'oder'           : 'or',
#                : 'pass',
#                : 'raise',
#                : 'return',
#                : 'try',
'solange'        : 'while',
'mit'            : 'with',
#                : 'yield'
}

functions = {
'druecken'       : 'print',
}

tokens = {}
tokens.update(keywords)
tokens.update(functions)

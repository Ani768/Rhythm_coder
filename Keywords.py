#Token types / constants

import operator
# Data Type
INT = 'INT'

# Operators
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULT'
DIVIDE = 'DIV'
EOF = 'EOF'
LPAREN = '('
RPAREN = ')'
LESS_THAN = 'LESS_THAN'
LESS_THAN_EQUAL = 'LESS_THAN_EQUAL'
EQUALS = 'EQUALS'
GREATER_THAN = 'GREATER_THAN'
GREATER_THAN_EQUAL = 'GREATER_THAN_EQUAL'

# Key Words
BEGIN = '{'
END = '}'
VERSE = 'VERSE'
INTERLUDE = 'INTERLUDE'
BRIDGE = 'BRIDGE'
PLAY = 'PLAY'
LOOP = 'LOOP'
CHORUS = 'CHORUS'
TRACK = 'TRACK'
RESOLVE = 'RESOLVE'

#Misc Tokens
SEMI = 'SEMI'
DOT = 'DOT'
ASSIGN = 'ASSIGN'
ID = 'ID'
STR = 'STR'
COMMA = ','


class Error:

  def __init__(self):
    self.res = []


class Token(object):#The tokeniser class

  def __init__(self, type, value, line=0):
    self.type = type
    self.value = value
    self.line = line

  def __str__(self):
    return 'Token({type}, {value})'.format(type=self.type,
                                           value=str(self.value))


RESERVED_KEYWORDS = {
    'BEGIN': Token('BEGIN', '{'),
    'END': Token('END', '}'),
    'VERSE': Token('VERSE', 'VERSE'),
    'INTERLUDE': Token('INTERLUDE', 'INTERLUDE'),
    'BRIDGE': Token('BRIDGE', 'BRIDGE'),
    'PLAY': Token('PLAY', 'PLAY'),
    'LOOP': Token('LOOP', 'LOOP'),
    'CHORUS': Token('CHORUS', 'CHORUS'),
    'TRACK': Token('TRACK', 'TRACK'),
    'RESOLVE': Token('RESOLVE', 'RESOLVE'),
}

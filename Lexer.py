from Keywords import *

#The starting of the Lexer class/Tokeniser
class Lexer(object):

  #Peeks one token ahead
  def peek(self):
    peek_pos = self.pos + 1
    if (peek_pos > len(self.text) - 1):
      return None
    else:
      return self.text[peek_pos]

  def __init__(self, text):
    self.text = text
    self.pos = 0
    self.line = 0
    self.col = 0
    self.err = Error()
    self.current_char = self.text[self.pos] if self.pos < len(
        self.text) else None

  #Advances to the next token
  def advance(self):
    self.pos += 1
    self.col += 1
    if self.pos > len(self.text) - 1:
      self.current_char = None
    else:
      self.current_char = self.text[self.pos]

  #Skips spaces
  def skip_space(self):
    while self.current_char is not None and self.current_char.isspace():
      self.advance()

  #returns an integer token(numeric)
  def integer(self):
    value = ''
    while self.current_char is not None and self.current_char.isdigit():
      value += self.current_char
      self.advance()
    return int(value)

  #Declaration of variable id's
  def _id(self):
    result = ''
    while self.current_char is not None and self.current_char.isalnum():
      result += self.current_char
      self.advance()
    token = RESERVED_KEYWORDS.get(result, Token(ID, result, self.line))
    token.line = self.line
    return token

  def error(self):#Error handling
    self.err.res.append('DISSONANCE DETECTED!!'+ '\n Wrong note:' +
                        self.current_char + '\n at line: ' + str(self.line))
    self.advance()

  #Processes a string 
  def get_str(self):
    self.advance()
    value = ""
    while self.current_char is not None and self.current_char is not "\"":
      value += self.current_char
      self.advance()
    self.advance()
    return str(value)

  def get_next_token(self):#The Tokeniser
    while self.current_char is not None:

      if self.current_char.isspace():
        self.skip_space()
        continue

      if self.current_char.isalpha():
        return self._id()

      if self.current_char.isdigit():
        return Token(INT, self.integer(), self.line)

      if self.current_char == '"':
        return Token(STR, self.get_str(), self.line)

      if self.current_char == '\n':
        self.advance()
        self.line += 1
        self.col = self.line
        continue

      if self.current_char == '+':
        self.advance()
        return Token(PLUS, '+', self.line)

      if self.current_char == ';':
        self.advance()
        return Token(SEMI, ';', self.line)

      if self.current_char == '-':
        self.advance()
        return Token(MINUS, '-', self.line)

      if self.current_char == '*':
        self.advance()
        return Token(MULTIPLY, '*', self.line)

      if self.current_char == '{':
        self.advance()
        return Token(BEGIN, '{', self.line)

      if self.current_char == '}':
        self.advance()
        return Token(END, '}', self.line)

      if self.current_char == '/':
        self.advance()
        return Token(DIVIDE, '/', self.line)

      if self.current_char == '=' and self.peek() == '=':
        self.advance()
        self.advance()
        return Token(EQUALS, '==', self.line)

      if self.current_char == '<' and self.peek() == '=':
        self.advance()
        self.advance()
        return Token(LESS_THAN_EQUAL, '<=', self.line)

      if self.current_char == '>' and self.peek() == '=':
        self.advance()
        self.advance()
        return Token(GREATER_THAN_EQUAL, '>=', self.line)

      if self.current_char == '=':
        self.advance()
        return Token(ASSIGN, '=', self.line)

      if self.current_char == '(':
        self.advance()
        return Token(LPAREN, '(', self.line)

      if self.current_char == ')':
        self.advance()
        return Token(RPAREN, ')', self.line)

      if self.current_char == ',':
        self.advance()
        return Token(COMMA, ',', self.line)

      if self.current_char == ';':
        self.advance()
        return Token(SEMI, ';', self.line)

      if self.current_char == '.':
        self.advance()
        return Token(DOT, '.', self.line)

      if self.current_char == '<':
        self.advance()
        return Token(LESS_THAN, '<', self.line)

      if self.current_char == '>':
        self.advance()
        return Token(GREATER_THAN, '>', self.line)

      self.error()
    return Token(EOF, None, self.line)

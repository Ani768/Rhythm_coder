# The starting of the AST classes and sub classes
#These are classes that aid the Parser and Interpreter


class AST(object):
  pass

#Class that represents a function definition(CHORUS)
class FUNC(AST):

  def __init__(self, token, name, var_param, body):
    self.token = token
    self.name = name.value
    self.body = body
    self.var_param = var_param
    self.val_param = []

#Class that represents a parameter(function's arguments)
class Param(AST):

  def __init__(self, token, val_param):
    self.token = token
    self.val_param = val_param

#Class that represent a function call(TRACK)
class Call(AST):

  def __init__(self, token, val_param, name):
    self.token = token
    self.name = name.value
    self.val_param = val_param

#Class that represents the return statement with it's value
class Return(AST):

  def __init__(self, token, value):
    self.token = token
    self.value = value

#Class that represent a compound block, the self.children is the list of nodes in the block
class Compound(AST):
  def __init__(self):
    self.children = []

#Class for binary operators
class BinaryOp(AST):

  def __init__(self, left, op, right):
    self.left = left
    self.token = op
    self.op = op
    self.right = right

#Class for Unary operators
class UnaryOp(AST):

  def __init__(self, op, expr):
    self.token = op
    self.op = op
    self.expr = expr

#Class for Assignment operators
class Assign(AST):

  def __init__(self, left, op, right):
    self.left = left
    self.token = self.op = op
    self.right = right

#Class for numberic values
class Num(AST):
  def __init__(self, token):
    self.token = token
    self.value = token.value

#class for Variables(ID's)
class Variable(AST):
  def __init__(self, token):
    self.token = token
    self.value = token.value

#Class representing the FOR block(LOOP)
class FOR_Block(AST):

  def __init__(self, token, assign, cond, change, body):
    self.token = token
    self.assign = assign
    self.cond = cond
    self.change = change
    self.body = body

#Class representing the IF block(VERSE)
class IF_Block(AST):

  def __init__(self, cond, token, if_body, elseif_nodes, else_body):
    self.cond = cond
    self.token = token
    self.if_body = if_body
    self.elseif_nodes = elseif_nodes
    self.else_body = else_body

#Class representing the ELSEIF block(BRIDGE)
class ELSEIF_Block(AST):

  def __init__(self, cond, token, body):
    self.cond = cond
    self.token = token
    self.body = body

#Class representing the PRINT statement(PLAY)
class Print(AST):

  def __init__(self, token, content):
    self.token = token
    self.content = content

#Class for empty statements
class NoOp(AST):
  pass

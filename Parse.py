from Lexer import *
from Keywords import *
from AST import *


""" 
    GRAMMAR:
        program: 
            CHORUS*

        func : 
            CHORUS ID (param) compound_statement

        RESOLVE exp|empty 
        
        param: 
            empty|(expr COMMA)*
        
        compound_statement: 
            BEGIN statement_list END
        
        statement_list : 
            (
                  assignment_statement 
                | empty
                | if_block
                | print 
                | for_block
                |expr
                |return 
            )*
        
        assignment_statement : 
            variable ASSIGN expr 
        
        empty :
        
        print : 
            PLAY( ((str|expr)COMMA)*  )  
        
        call : 
            TRACK ID (param)

        if_block: 
            VERSE expr 
                compound_statement 
            | (INTERLUDE
                compound_statement)*
            | BRIDGE
                compount_statement
            | empty

    
        elseif_block:
            INTERLUDE expr 
                compound_statement 
    
        for_block: 
            LOOP(assignment_statement, cond, change) 
                compounf_statement


        factor :
             PLUS factor
           | MINUS factor
           | INTEGER
           | LPAREN expr RPAREN
           | variable
           | call

        term: 
            factor (
                        (
                             MUL 
                            | DIV 
                            | LESS_THAN 
                            | LESS_THAN_EQUAL 
                            | EQUALS 
                            | GREATER_THAN 
                            | GREATER_THAN_EQUAL
                        ) 
                    factor  
                    )*

        expr: 
            term (
                    (
                          PLUS 
                        | MINUS
                    ) 
                 term
                 )*

    
        variable: 
            ID 
"""




class Parser(object):
    def __init__(self, lexer):
        self.lexer = lexer
        # set current token to the first token taken from the input
        self.current_token = self.lexer.get_next_token()

    def error(self, expected, detected):
        
        self.lexer.err.res.append('DISSONANCE DETECED!! This is not jazz, do not change the scale mate!'
                        +'\n      Expected: '+expected
                        +'\n      Recieved: '+ detected
                        +'\n      At line:  '+str(self.lexer.line
                        ))
    
    def eat(self, token_type):
        # compare the current token type with the passed token
        # type and if they match then "eat" the current token
        # and assign the next token to the self.current_token,
        # otherwise raise an exception.
        
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            # okay, so if we got mis-match, this is going to be an error()
            # just eat what you want now, and move on - simple remedy, but not the best or correct one
            # works 65% of the time, gives un reasonable results 35% of the times
            self.error(token_type,self.current_token.type)
            self.eat(self.current_token.type)
            return


    def program(self):
        """
        program: CHORUS*
        """
        result = []
        while self.current_token.type == CHORUS:
            node=self.func()
            result.append(node)

        return result
    
    def func(self):
        """
        func : CHORUS ID (param) compound_statement  
        """
        token=self.current_token
        self.eat(CHORUS)
        name = self.variable()
        self.eat(LPAREN)
        var_param = self.param(1)
        self.eat(RPAREN)
        body = self.compound_statement()
        return FUNC(token, name, var_param, body)

    def ret(self):
        """
        RESOLVE exp|empty 
        """
        token=self.current_token
        self.eat(RESOLVE)
        if(self.current_token.type in (ID,PLUS,MINUS,INT,LPAREN,TRACK)):
            node = self.expr()
            return Return(token,node)

        
        node = NoOp()
        return Return(token,node)

    def param(self, expected):
        """
        param: empty|(expr COMMA)*
        """

        # to tell me, if the param list is only variables, or only values
        # if function recieved paramter 1 - then im execting strictly variables,
        # else I am expecting expressions

        ok1 = ok2 = 0
        token=self.current_token
        node = self.empty()

        result = []
        while(self.current_token.type in (ID, PLUS, MINUS, LPAREN, INT, TRACK)):
            if(expected == 1):
                node = self.variable()
                ok1=1
            elif(expected==2):
                node = self.expr()
                ok2=1
            result.append(node)
            self.eat(COMMA)

        if(ok1+ok2 == 2):
            raise Exception("HARMONY MISMATCH DETECTED!!Two different melodies at the same time? Please keep away from polyrhythms!")
        elif(ok1+ok2==0):
            return result
        else:
            if(expected==1 and ok1==1):
                return result
            elif(expected==2 and ok2==1):
                return result
            else:
                raise Exception('It seems you have not matched the melody which the song expects. Please match the melody and try again!')

    def compound_statement(self):
        """
        compound_statement: BEGIN statement_list END
        """
        self.eat(BEGIN)
        nodes = self.statement_list()
        self.eat(END)
        root = Compound()
        for node in nodes:
            root.children.append(node)
        return root

    def statement_list(self):
        """
        statement_list : (assignment_statement | empty| IF_Block| print | for_block|expr|return )*
        """
        node=self.empty()
        result=[node]
        while(self.current_token.type in (ID, VERSE, PLAY, LOOP, TRACK, RESOLVE)):
            if self.current_token.type == ID:
                node = self.assignment_statement()
                self.eat(SEMI)
            elif self.current_token.type == VERSE:
                node = self.IF_Block()
            elif self.current_token.type == LOOP:
                node = self.for_block()    

            elif self.current_token.type == PLAY:
                node = self.print()
                self.eat(SEMI)
            elif self.current_token.type == TRACK:
                node = self.call()
                self.eat(SEMI)
            elif self.current_token.type == RESOLVE:
                node = self.ret()
                self.eat(SEMI)
                
            result.append(node)
        
        return result

    def assignment_statement(self):
        """
        assignment_statement : variable ASSIGN expr
        """
        left = self.variable()
        token = self.current_token
        self.eat(ASSIGN)
        right = self.expr()
        node = Assign(left, token, right)
        return node

    def empty(self):
        """
        An empty production
        """
        return NoOp()

    def print(self):
        """ 
        PLAY( ((str|expr)COMMA)*  ) 
        """
        token = self.current_token
        node = self.empty()
        result = [node]
        self.eat(PLAY)
        self.eat(LPAREN)
        while(self.current_token.type in (STR, ID, PLUS, MINUS,INT, LPAREN, TRACK)):
            if(self.current_token.type == STR):
                node = self.current_token.value
                self.eat(STR)
            elif(self.current_token.type in (ID, PLUS, MINUS,INT, LPAREN, TRACK)):
                node = self.expr()

            result.append(node)
            self.eat(COMMA)

        self.eat(RPAREN)
        

        return Print(token, result)
    
    def call(self):
        """
        call : TRACK ID (param)
        """
        token=self.current_token
        self.eat(TRACK)
        name = self.variable()
        self.eat(LPAREN)
        val_param = self.param(2)
        self.eat(RPAREN)

        return Call(token, val_param, name)

    def IF_Block(self):
        """ 
        IF_Block: VERSE expr 
                    compound_statement 
                | (BRIDGE
                    compound_statement)*
                | INTERLUDE
                    compount_statement
                | empty
        """
        token = self.current_token
        self.eat(VERSE)
        cond = self.expr()
        if_body = self.compound_statement()
        elseif_nodes=[]
        while (self.current_token.type == BRIDGE):
            elseif_nodes.append(self.ELSEIF_Block())

        if(self.current_token.type == INTERLUDE):
            self.eat(INTERLUDE)
            else_body = self.compound_statement()
        else:
            else_body = self.empty()

        node= IF_Block(cond, token, if_body, elseif_nodes, else_body)
        return node

    def ELSEIF_Block(self):
        """ 
        elseIF_Block: BRIDGE expr compound_statement 
        """
        token = self.current_token
        self.eat(BRIDGE)
        cond = self.expr()
        body = self.compound_statement()
        
        node= ELSEIF_Block(cond, token, body)
        return node

    def for_block(self):
        """
            for_block: LOOP(assignment_statement COMMA cond COMMA change COMMA) 
                            compound_statement
        """
        token = self.current_token
        self.eat(LOOP)
        self.eat(LPAREN)
        assig = self.assignment_statement()
        self.eat(COMMA)
        cond = self.expr()
        self.eat(COMMA)
        change = self.assignment_statement()
        self.eat(COMMA)
        self.eat(RPAREN)
        body = self.compound_statement()
        return FOR_Block(token,assig,cond,change,body)

    def factor(self):
        """
        factor : (PLUS | MINUS) factor | INTEGER | LPAREN expr RPAREN | call

        """
        token = self.current_token
        if token.type == PLUS:
            self.eat(PLUS)
            node = UnaryOp(token, self.factor())
            return node
        elif token.type == MINUS:
            self.eat(MINUS)
            node = UnaryOp(token, self.factor())
            return node
        elif(token.type==INT):
            self.eat(INT)
            return Num(token)
        elif(token.type==LPAREN):
            self.eat(LPAREN)
            node = self.expr()
            self.eat(RPAREN)
            return node
        elif(token.type==TRACK):
            node = self.call()
            return node
        else:
            node = self.variable()
            return node

    def term(self):
        """
        term: factor ((MUL | DIV | LESS_THAN | LESS_THAN_EQUAL | EQUALS | GREATER_THAN | GREATER_THAN_EQUAL) factor)*
        """
        node = self.factor()

        while self.current_token.type in (MULTIPLY, DIVIDE, LESS_THAN, LESS_THAN_EQUAL, EQUALS, GREATER_THAN, GREATER_THAN_EQUAL):
            token = self.current_token

            if token.type == MULTIPLY:
                self.eat(MULTIPLY)
            elif token.type == DIVIDE:
                self.eat(DIVIDE)
            elif token.type == LESS_THAN:
                self.eat(LESS_THAN)
            elif token.type == LESS_THAN_EQUAL:
                self.eat(LESS_THAN_EQUAL)
            elif token.type == EQUALS:
                self.eat(EQUALS)
            elif token.type == GREATER_THAN: 
                self.eat(GREATER_THAN)
            elif token.type == GREATER_THAN_EQUAL:
                self.eat(GREATER_THAN_EQUAL)

            node = BinaryOp(left=node, op=token, right=self.factor())

        return node

    def expr(self):
        """
        expr   : term ((PLUS | MINUS) term)*
        """
        node = self.term()

        while self.current_token.type in (PLUS, MINUS):
            token = self.current_token
            if token.type == PLUS:
                self.eat(PLUS)
            elif token.type == MINUS:
                self.eat(MINUS)

            node = BinaryOp(left=node, op=token, right=self.term())
        
        return node

    def variable(self):
        """
        variable : ID
        """
        node = Variable(self.current_token)
        self.eat(ID)
        return node

    def parse(self):
        node = self.program()
        if self.current_token.type != EOF:
            self.error(EOF,self.current_token.type)
        return node

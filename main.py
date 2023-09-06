import operator
from Interpreter import *

def main():
  text = """
      CHORUS factorial(n,){
            VERSE(n==0){
              RESOLVE 1;
            }
            RESOLVE n*TRACK factorial(n-1,);
          }

          CHORUS SONG(){
              PLAY("Here's a simple example of a recursive code","\n",);
              PLAY(TRACK factorial(4,),"\n",);
              PLAY(TRACK factorial(7,),"\n",);
            
          }      
                      
                                     
     """
  lexer = Lexer(text)
  parser = Parser(lexer)
  interpreter = Interpreter(parser)
  interpreter.interpret()


if __name__ == '__main__':
  main()

  # Rhythmcoder - Anirudh S
          


Rhythmcoder is a programming language that was built entirely from scratch in 2 weeks. There are no additional libraries that need to be installed for the language. It includes a lot of functionalities that a normal programming language has. The language was developed to gain a better insight of how interpreters work. Here, I've made it interpret a programming language of my choice. I've added music as a personal touch to the language.

Some of its features include:

- Local Namespace handling
- Recursive function calls
- Unique music-based syntax
- Error handling + special music prompts
- Basic mathematical expressions and operations
- Looping and conditional constructs (For and if-else if-else)
- Functions with parameters and calls

## Here are some examples of sample codes and outputs

Note: The text is the input which is further passed through a Lexer, Parser, and Interpreter, which then interprets and produces the output.

```python
text = """
CHORUS SONG(){
    PLAY("Hello World!",);
}
"""
```

**OUTPUT:** <br/> 
Hello World! <br/> 
SONG PLAYED IN PERFECT HARMONY!!! <br/> 

**The below code demonstrates the If-Else If-Else construct:**
```python
text = """
    CHORUS SONG(){
    a=23;
    VERSE(a<5) {
        PLAY("a is lesser than 5",);
    }
    BRIDGE(a<=20){
        PLAY("a is between 5 and 20",);
    }
    INTERLUDE{
        PLAY("a is greater than 20",);
    }
}
"""
```
**OUTPUT:**  <br/> 
a is greater than 20  <br/> 
SONG PLAYED IN PERFECT HARMONY!!! <br/> 

**I have used the same code as before to demonstrate error handling:**
```python
text = """
CHOR SONG(){
    a=23;
    VERSE(a<5) {
        PLAY("a is between 5 and 15",);
    }
    BRIDGE(a<=20){
        PLAY("a is between 5 and 20",);
    }
    INTERLUDE{
        PLAY("a is greater than 20",);
    }
}
"""
```

**OUTPUT:**  <br/> 
The SONG has slight dissonances here and there, about 2 in total!!!! Prepare for <br/>  trouble and make it double!! 🎵🎵 <br/> 
1: DISSONANCE DETECTED!! This is not jazz, do not change the scale mate! <br/> 
Expected: EOF Received: ID At line: 0 <br/> 
2: Invalid Song Name – COMPOSITION ERROR Song does not exist <br/> 

**The below code demonstrates looping statements:**
```python
text = """
CHORUS SONG(){
    n=4;
    LOOP(i=0,i<n,i=i+1,) {
        PLAY("The value of n during iteration ",i+1," is: ",n*i,"\n",);
    }
}
"""
```
**OUTPUT:** <br/> 
The value of n during iteration 1 is: 0 <br/> 
The value of n during iteration 2 is: 4 <br/> 
The value of n during iteration 3 is: 8 <br/> 
The value of n during iteration 4 is: 12 <br/> 
SONG PLAYED IN PERFECT HARMONY!!! <br/> 


**The below code demonstrates recursion:**
```python
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
```
**OUTPUT**<br/> 
Here's a simple example of a recursive code<br/> 
24<br/> 
5040<br/> 
<br/> 
SONG PLAYED IN PERFECT HARMONY!!!<br/> 

**To run my project, click [this link](https://replit.com/@AnirudhSivakum2/Rhythmcoder?v=1).**
 

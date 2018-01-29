Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> Number =input ("Enter your number")
Enter your number12
>>> Number
'12'
>>> 
>>> Number = int (input ("Enter your number"))
Enter your number12
>>> Number
12
>>> help(input)
Help on built-in function input in module builtins:

input(prompt=None, /)
    Read a string from standard input.  The trailing newline is stripped.
    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.

>>> hrlp (str)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    hrlp (str)
NameError: name 'hrlp' is not defined
>>> import os
>>> os.system('cls')
0
>>> import os
>>> os.system('cls')
0
>>> num1=int(input("Enter num 1"))
Enter num 122
>>> num2=int(input("Enter num 2"))
Enter num 223
>>> print("Addition ",num1+num2)
Addition  45
>>> name=input("Enter name")
Enter nameHimanshu
>>> print("Addition",num1+num2,name")
	  
SyntaxError: EOL while scanning string literal
>>> print("Addition",num1+num2,name)
	  
Addition 45 Himanshu
>>> 

Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # OPERATORS
>>> # Arithmetic Operators-> +,-,*,// (integer division), /, % (modulus), **
>>> # Assignment Operators-> +=, -=, *=, //=, /=, %=, **=
>>> # Comparison Operators-> <,>,<=,>=,!=,==
>>> # Logical Operators-> and,or,not
>>> # Identify Operators-> is, is not
>>> # Membership Operators-> in, not in
>>> # Bitwise Operators-> &, |, ~, ^, <<, >>
>>> 
>>> #ARITHMETIC
>>> a=4
>>> b=6
>>> print(a+b)
10
>>> print(a-b)
-2
>>> print(a*b)
24
>>> print(a//b)
0
>>> print(a/b)
0.6666666666666666
>>> print(a%b)
4
>>> print(a**b)
4096
>>> 
>>> #ASSIGNMENT
>>> a=3
>>> b=4
>>> print(a+=b)  #It raises an error because we cannot directly print the updated value)
SyntaxError: invalid syntax
>>> b+=a
>>> b # or print(b). In an interpreter we can just call the variable instead of using print statement
7
>>> b-=a
>>> b
4
>>> b*=a
>>> b
12
>>> b//=a
>>> b
4
>>> b/=a
b
1.3333333333333333
b%=a
b
1.3333333333333333
b**=a
b
2.37037037037037

a+=b
a
5.37037037037037
del (a,b)
a=3
b=4
a+=b
a
7
a-=b
a
3
a*=4
a
12
a//=4
a
3
a/=2
a
1.5
a%=b
a
1.5
a**=4
a
5.0625

# COMPARISION
a=6
b=8
a<b
True
a>b
False
a<=b
True
a>=b
False
a!=b
True
a==b
False
b>=a
True
b<=a
False
b<a
False
b>a
True
a= 9
b=9
a==b
True
a!=b
False

# LOGICAL
a=
SyntaxError: incomplete input
a=7
b=11
a<b and b>a
True
a<=b and b>=a
True
a!=b and a==b
False
a<b or b>a
True
a<=b or b>=a
True
a!=b or a==b
True
not True
False
not False
True

# IDENTIFY
a=5
if type(a) is int:
    print('It is int')

It is int
if type(a) is not int:
    print('It is not int')

    
b=9
del b
b=9.3
if type(b) is int:
    print('True')

    
if type(b) is not int:
    print('True')

    
True

# MEMBERSHIP
a=5,67,33,56,78,89, 90, 10
if 33 in a:
    print(33)

    
33
if 33 not in a:
    print(33)

    
if 32 not in a:
    print(32)

    
32
if 32 in a:
    print(32)

    
# BITWISE
a=6
b=5
a&b
4
bin(a)
'0b110'
bin(5)
'0b101'
a|b
7
a^b
3
~a
-7
~b # Formula for ~: -(b+1)
-6
a<<b
192
a>>b
0
# For << , the logic is to add b no. of bits at the right of a bit

# Example: a=6 -> 0110, b=2 -> 0010
# a<<b 0110+00 -> 011000 which is 24 the final answer
a=6
a>>2
1
# For >>, the logic is to discard bits
# Example: a=6, need to find a>>2
# binary of 6 is 0110, in the right end of the 6 bit we'll delete 2 bits since it is given
# Then the answer will be 01 which is 1

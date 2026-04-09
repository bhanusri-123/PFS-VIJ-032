Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# DATATYPE CONVERSION
#int()
int(8)
8
int(5.5)
5
int("bhanu")
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    int("bhanu")
ValueError: invalid literal for int() with base 10: 'bhanu'
int(6+9j)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int(6+9j)
TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'
int(True)
1
int(False)
0
# float()
float(5)
5.0
float(6.6)
6.6
float("bhanu")
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    float("bhanu")
ValueError: could not convert string to float: 'bhanu'
float(5+4j)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    float(5+4j)
TypeError: float() argument must be a string or a real number, not 'complex'
float(True)
1.0
float(False)
0.0
# str()
str(4)
'4'
str(4.7)
'4.7'
str("bhanu")
'bhanu'
str(4+5j)
'(4+5j)'
>>> str(True)
'True'
>>> str(False)
'False'
>>> #complex()
>>> complex(4)
(4+0j)
>>> complex(5.5)
(5.5+0j)
>>> complex("bhanu")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    complex("bhanu")
ValueError: complex() arg is a malformed string
>>> complex(3+4j)
(3+4j)
>>> complex(True)
(1+0j)
>>> complex(False)
0j
>>> #bool()
>>> boole(4)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    boole(4)
NameError: name 'boole' is not defined. Did you mean: 'bool'?
>>> bool(4)
True
>>> bool(4.4)
True
>>> bool("Bhanu")
True
>>> bool(4+5j)
True
>>> bool(True)
True
>>> bool(False)
False

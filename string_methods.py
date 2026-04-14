Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#STRING METHODS
#Python completely depends on Strings

# len()
a="python"
len(a)
6
b="python course"
len(b)
13
c=""
len(c)
0
d=" "
len(d)
1

#count() - no. of repeated characters or words
a="twinkle twinkle little star"
count(a)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    count(a)
NameError: name 'count' is not defined. Did you mean: 'round'?
a.count("twinkle")
2
a.count("t")
5
a.count("l")
4
a.count(" ")
3
a.count("e")
3
a.count("le")
3
a.count("ni")
0

#find a string
a="code"
a[1] #indexing
'o'
a.find("e")
3
a.find("c")
0
a.find("n")
-1
b="codegnan"
b.find("n")
5
b.find("d")
2
b.find("r")
-1

#escape sequences
#\n -> new line or next line
#\t -> tab space(4 spaces)
a="name \nmobileno \tmail id\n address"
print(a)
name 
mobileno 	mail id
 address
a="name \nmobileno \tmail id\naddress"
print(a)
name 
mobileno 	mail id
address
b="name: Bhanusri\nmobileno:7569133943\tmail id:bhanusri.venigalla03@gmail.com\naddress:vijayawada"
print(b)
name: Bhanusri
mobileno:7569133943	mail id:bhanusri.venigalla03@gmail.com
address:vijayawada

#replace()
a="wait until you succeed"
a.replace("wait","work")
'work until you succeed'
b="My name is V.Bhanusri"
b.replace("My","Her")
'Her name is V.Bhanusri'

#upper()
a="code"
a.upper()
'CODE'
#lower()
a="PYTHON COURSE"
a.lower()
'python course'

#capitalize
a="python"
a.capitalize()
'Python'
b="python course"
b.capitalize()
'Python course'
#title()
a="python course"
a.title()
'Python Course'
b="my name is v.bhanusri"
b.title()
'My Name Is V.Bhanusri'
c="i am in class"
c.title()
'I Am In Class'

#isupper() and islower()
a="python"
a.isupper()
False
a.islower()
True
#startswith() and endswith()
a.startswith("h")
False
a.startswith("p")
True
a.endswith("n")
True
#isalpha()
a.isalpha()
True
b="python course"
b.isalpha()
False
#false because space is not an alphabet
b="pythoncourse"
b.isalpha()
True

#isdigit()
d=345342
d.isdigit()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d.isdigit()
AttributeError: 'int' object has no attribute 'isdigit'
d="24231"
d.isdigit()
True
#isalnum
d="python123"
d.isalnum()
True
d="bhanu@1234"
d.isalnum()
False

#split()
a="java c c++ python R"
a.split()
['java', 'c', 'c++', 'python', 'R']
b="i am learning python full stack course at codegnan e-learning institute"
b.split()
['i', 'am', 'learning', 'python', 'full', 'stack', 'course', 'at', 'codegnan', 'e-learning', 'institute']
c="23242 42423"
c.split()
['23242', '42423']

#join()
a="vja","hyd","vzg"
"".join(a)
'vjahydvzg'
" ".join(a)
'vja hyd vzg'

#strip()
#Used to remove white spaces
#2 types - lstrip(),rstrip()
a="      bhanusri       "
a.strip()
'bhanusri'
a.lstrip()
'bhanusri       '
a.rstrip()
'      bhanusri'

#concatenation
a="python"
b="course"
print(a+b)
pythoncourse
>>> print(a+" "+b)
python course
>>> fname="venigalla"
>>> lname="bhanusri"
>>> print(fname+lname)
venigallabhanusri
>>> print(fname+" "+lname)
venigalla bhanusri
>>> print(fname.title()+" "+lname.title())
Venigalla Bhanusri
>>> #Instead of that we can do this
>>> print((fname+" "+lname).title())
Venigalla Bhanusri
>>> #formatting - adding an additional string
>>> a=34
>>> b=45
>>> print("The sum of two given numbers is", a+b)
The sum of two given numbers is 79
>>> print("The sum of",a,"and",b,"is", a+b)
The sum of 34 and 45 is 79
>>> 
>>> #format()
>>> a="motu"
>>> b="patlu"
>>> print("Hello {}{}".format())
Traceback (most recent call last):
  File "<pyshell#140>", line 1, in <module>
    print("Hello {}{}".format())
IndexError: Replacement index 0 out of range for positional args tuple
>>> print("Hello {}{}".format(a,b))
Hello motupatlu
>>> print("Hello {} {}".format(a,b))
Hello motu patlu
>>> print("Hello {} Hello {}".format(a,b))
Hello motu Hello patlu
>>> 
>>> #fstring
>>> a="chota"
>>> b="bheem"
>>> print(f"Hello {a}{b}")
Hello chotabheem
>>> print(f"Hello {a} Hello {b}")
Hello chota Hello bheem
>>> print(f"Hello {a}{b}")
Hello chotabheem

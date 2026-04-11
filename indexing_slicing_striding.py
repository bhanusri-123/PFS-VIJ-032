Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#INDEXING
a='vijayawada'
a[0]
'v'
a[1]
'i'
a[2]
'j'
a[3]
'a'
a[0]+a[1]+a[2]+a[3]+a[4]+a[5]
'vijaya'
b="i am in class"
b[8]+b[9]+b[10]+b[11]+b[12]
'class'
b[2]+b[3]
'am'
b[5]+b[6]
'in'
c="i am learning python"
a[2]+a[3]
'ja'
c[2]+c[3]
'am'
c[5]+c[6]+c[7]+c[8]+c[9]
'learn'
c[14]+c[15]+c[16]+c[17]+c[18]+c[19]
'python'
d="i am in work"
d[5]+d[6]
'in'
d[8]+d[9]+d[10]+d[11]
'work'
d[2]+d[3]
'am'
e="simple is better than complex"
e[-1]+e[-2]+e[-3]+e[-4]+e[-5]+e[-6]+e[-7]
'xelpmoc'
e[-7]+e[-6]+e[-5]+e[-4]+e[-3]+e[-2]+e[-1]
'complex'
e[-19]+e[-18]+e[-17]+e[-16]+e[-15]+e[-14]
'better'
e[-29]+e[-28]+e[-27]+e[-26]+e[-25]+e[-24]
'simple'
f="codegnan it solutions"
f[-9]+f[-8]+f[-7]+f[-6]+f[-5]+f[-4]+f[-3]+f[-2]+f[-1]
'solutions'
f[-12]+f[-11]
'it'
f[-21]+f[-20]+f[-19]+f[-18]+f[-17]+f[-16]+f[-15]+f[-14]
'codegnan'

#SLICING
a="codegnan"
a[0:3]
'cod'
a[0:4] #if we want "code" to print, then we have to add an extra number 3->4
'code'
a[4:8]
'gnan'
a[:4]
'code'
#The above one is the prefix
a[4:] #And this is the suffix
'gnan'

b="work hard until you succeed"
b[15:18]
' yo'
b[15:19]
' you'
b[20:27]
'succeed'
b[9:14]
' unti'
b[9:15]
' until'
b[0:4]
'work'
b[5:9]
'hard'

c="beautiful is better than ugly"
c[13:19]
'better'
b[25:29]
'ed'
c[25:29]
'ugly'
c[0:9]
'beautiful'

d="patience is strength"
d[-1:-9]
''
d[-9:-1]
' strengt'
d[-9:0]
''
d[-9:-0]
''
d[-9:]
' strength'
d[-8:]
'strength'
d[:-12]
'patience'
d[-13:-21]
''
d[-12:-21]
''

e="sun rises in the east"
e[-6:-9]
''
e[-8:-5]
'the'
e[-5:]
' east'
e[-4:]
'east'
e[:-18]
'sun'
e[-21:-18]
'sun'
e[-17:-12]
'rises'

#STRIDING
# Syntax: [a:b:c]  Here a-starting, b-ending, c-increment
a="Data Science"
a[::]
'Data Science'
a[::1]
'Data Science'
>>> a{::2]
SyntaxError: closing parenthesis ']' does not match opening parenthesis '{'
>>> a[::2]
'Dt cec'
>>> b="Cloud Computing"
>>> b[::5]
'C u'
>>> b[::3]
'CuCpi'
>>> b[3:]
'ud Computing'
>>> b[5:11]
' Compu'
>>> b[:9]
'Cloud Com'
>>> [::7]
SyntaxError: invalid syntax
>>> b[::7]
'Cog'
>>> b[::2]
'CodCmuig'
>>> c="machine learning"
>>> c[1:9:2]
'ahn '
>>> c[2:14:3]
'cnlr'
>>> c[3:15:5]
'hli'
>>> c[3:13:4]
'h r'
>>> c[2:12:6]
'cl'
>>> d="python course"
>>> d[-1:-9:-3]
'eu '
>>> d[-4:-12:-4]
'un'
>>> d[-3:-14:-2]
'ro otp'
>>> # In positive striding, the starting and ending index should range from lowest to highest and not highest to lowest
>>> # In lowest striding, the starting and ending index should range from highest to lowest and not lowest to highest
>>> d[::-1] # String Reverse
'esruoc nohtyp'
>>> d[::1]
'python course'

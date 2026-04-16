Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#LIST
a=[2,3.33,'bhanu',5+4j,True,False]
print(a)
[2, 3.33, 'bhanu', (5+4j), True, False]
type(a)
<class 'list'>
b=9.0
type(b)
<class 'float'>
c=[9.0]
type(c)
<class 'list'>

#LIST METHODS
#append()
a=["java","c","c++"]
a.append("python")
print(a)
['java', 'c', 'c++', 'python']
a.append('ML')
a
['java', 'c', 'c++', 'python', 'ML']
a.append('ds','ai')
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a.append('ds','ai')
TypeError: list.append() takes exactly one argument (2 given)
a.append(['ds','ai'])
a
['java', 'c', 'c++', 'python', 'ML', ['ds', 'ai']]
#extend() - can add one or more values into a list
a=['vja','vzg']
a.extend(['hyd','prdt'])
a
['vja', 'vzg', 'hyd', 'prdt']
#insert() - adds a value in a particular position
a=['vja','vzg']
a.insert(1,'hyd')
a
['vja', 'hyd', 'vzg']
a[2]
'vzg'
#index()
a.index('vzg')
2
#copy()
a.copy()
['vja', 'hyd', 'vzg']
#clear()
a.clear()
a
[]
#sort()
a=['banana','apple','mango','guava','dragon fruit']
a.sort()
a
['apple', 'banana', 'dragon fruit', 'guava', 'mango']
b=[3,45,7,2,7,5,9]
b.sort()
b
[2, 3, 5, 7, 7, 9, 45]
>>> #reverse()
>>> a=['python','java','c','c++']
>>> a.reverse()
>>> a
['c++', 'c', 'java', 'python']
>>> b=[3,4,7,5,9,6,2,1]
>>> b.reverse()
>>> b
[1, 2, 6, 9, 5, 7, 4, 3]
>>> b.sort()
>>> b
[1, 2, 3, 4, 5, 6, 7, 9]
>>> b.reverse() #now we'll get it in descending order
>>> b
[9, 7, 6, 5, 4, 3, 2, 1]
>>> #pop()
>>> a=['black','white','red']
>>> a.pop() #here we didn't specify what element to pop, so by default it pops the last element
'red'
>>> a
['black', 'white']
>>> a.pop('black')
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a.pop('black')
TypeError: 'str' object cannot be interpreted as an integer
>>> a.pop(0)
'black'
>>> a
['white']
>>> #remover()
>>> #remove()
>>> a=['chocolates','sweets','cadbury']
>>> a.remove('sweets')
>>> a
['chocolates', 'cadbury']
>>> #count()
>>> a.count('chocolates')
1
>>> b='python'
>>> len(b)
6
>>> c=['python']
>>> len(c)
1
>>> #List is mutable (we can change anything)

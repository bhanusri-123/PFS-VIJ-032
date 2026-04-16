Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #TUPLE
>>> #Tuple is immutable (we cannot change anything so we don't have any methods)
>>> a=(3,4.5,'python',4+6j,True,False)
>>> print(a)
(3, 4.5, 'python', (4+6j), True, False)
>>> type(a)
<class 'tuple'>
>>> a.count('python')
1
>>> a.index(True)
4
>>> a.index('python')
2
>>> a.index(3)
0
>>> 
>>> #SETS {}
>>> #Set is semi-mutable and it is an unordered collection. It doesn't allow duplicate values
>>> a={3,5.6,'bhanu',3+5j,True,False}
>>> print(a)
{False, True, (3+5j), 3, 5.6, 'bhanu'}
>>> type(a)
<class 'set'>
>>> b={3,5,1,4,6,9,10}
>>> type(b)
<class 'set'>
>>> print(b)
{1, 3, 4, 5, 6, 9, 10}
>>> #python set methods
>>> #add()
>>> a={4,6,87,23,5}
>>> a.add(24)
>>> a
{4, 5, 6, 23, 87, 24}
>>> #issubset()
>>> a={1,2,3,4,5,6}
>>> b={1,2,4}
>>> b.issubset(a)
True
>>> a.issubset(b)
False
>>> #issuperset()
>>> a={1,2,3,4,5,6}
>>> b={4,5,6}
>>> b.issuperset(a)
False
a.issuperset(b)
True
#union() - merging of two sets
a={3,4,5,6,2}
b={5,6,7,8,10}
a.intersection(b)
{5, 6}
a.union(b)
{2, 3, 4, 5, 6, 7, 8, 10}
#intersection()
a={2,3,4,5,1,9,8,6}
b={3,5,9,10}
a.intersection(b)
{9, 3, 5}
#difference()
a={1,2,3,5,6,8}
b={4,5,6,7,8}
a.difference(b)
{1, 2, 3}
b.difference(a)
{4, 7}
#update()
a={1,2,3,4,6,7}
b={5,6,7,8,9,11}
a.update(b)
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
a
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
b.update(a)
b
{1, 2, 3, 4, 5, 6, 7, 8, 9, 11}
#symmetric_difference()
a={3,4,5,6,7,8,9,10}
b={5,6,7,8,9,10,11,12}
a.symmetric_difference(b)
{3, 4, 11, 12}
b.symmetric_difference(a)
{3, 4, 11, 12}
#difference_update()
a={11,12,13,14,15,16}
b={7,8,9,10,11,12,13}
a.difference_update(b)
a
{16, 14, 15}
b.difference_update(a)
b
{7, 8, 9, 10, 11, 12, 13}
#intersection_update()
a={2,3,4,5,6,7,8,9,10}
b={4,5,6,8,7,9,10,11}
a.intersection_update(b)
a
{4, 5, 6, 7, 8, 9, 10}
b.intersection_update(a)
b
{4, 5, 6, 7, 8, 9, 10}
#symmetric_difference_update()
a={3,4,5,6,7,8,9,10,11,12}
b={1,2,3,4,5,6,7,8,9,10}
a.symmetric_difference_update(b)
a
{1, 2, 11, 12}
b.symmetric_difference_update(a)
b
{3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
#pop()
a={1,2,3,4,5,6}
a.pop()
1
a.pop(3)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    a.pop(3)
TypeError: set.pop() takes no arguments (1 given)
a.remove(3)
a
{2, 4, 5, 6}
#discard()
a.a={5,6,7,8}
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    a.a={5,6,7,8}
AttributeError: 'set' object has no attribute 'a'
#discard()
a={5,6,7,8}
a.discard(8)
a
{5, 6, 7}
a.copy()
{5, 6, 7}
b=a.copy()
b
{5, 6, 7}
#clear()
a={7,8,9,10}
a.clear()
a
set()
b=set()
b.add(30)
b
{30}






















#isdisjoint()
a={5,6,7,8,9,0}
b={1,2,3,4,5}
a.isdisjoint(b)
False
a={1,2,3,4,5,6}
b={7,8,9,10,11}
a.isdisjoint(b)
True

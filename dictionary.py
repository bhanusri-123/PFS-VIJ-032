Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #DICTIONARY
>>> #dict{}
>>> a={"place":"vijayawada","age":21,"year":2005}
>>> a
{'place': 'vijayawada', 'age': 21, 'year': 2005}
>>> type(a)
<class 'dict'>
>>> b={"place","age","year"}
>>> b
{'year', 'age', 'place'}
>>> type(b)
<class 'set'>
>>> 
>>> #METHODS
>>> a.keys()
dict_keys(['place', 'age', 'year'])
>>> a.values()
dict_values(['vijayawada', 21, 2005])
>>> a.items()
dict_items([('place', 'vijayawada'), ('age', 21), ('year', 2005)])
>>> #accessing
>>> a={"year":2026,"month":4,"date":16}
>>> a["year"]
2026
>>> #update()
>>> a.update({"time":5})
>>> a
{'year': 2026, 'month': 4, 'date': 16, 'time': 5}
>>> a.update({"time":3},{"min":10})
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a.update({"time":3},{"min":10})
TypeError: update expected at most 1 argument, got 2
>>> a.update({"time":3,"min":19})
>>> a
{'year': 2026, 'month': 4, 'date': 16, 'time': 3, 'min': 19}
>>> #setdefault()
>>> a.setdefault("city","vijayawada")
'vijayawada'
>>> a
{'year': 2026, 'month': 4, 'date': 16, 'time': 3, 'min': 19, 'city': 'vijayawada'}
>>> #pop()
>>> a.pop()
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
a.pop("city")
'vijayawada'
a
{'year': 2026, 'month': 4, 'date': 16, 'time': 3, 'min': 19}
#popitem()
a.popitem()
('min', 19)
a
{'year': 2026, 'month': 4, 'date': 16, 'time': 3}
#copy()
a.copy()
{'year': 2026, 'month': 4, 'date': 16, 'time': 3}
#get()
a.get("year")
2026
a.get("year","month")
2026
#clear()
a.clear()
a
{}
b={}
b.update({"name":"bhanusri"})
b
{'name': 'bhanusri'}

a={"year":2026,"month":"april","name":"bhanu","name":"bhanu"}
a
{'year': 2026, 'month': 'april', 'name': 'bhanu'}
b={"year":2026,"month":"april","name":"bhanu","name":"pooja"}
b
{'year': 2026, 'month': 'april', 'name': 'pooja'}
a={"year":2026,"month":"april","name":"bhanu","name1":"bhanu"}
a
{'year': 2026, 'month': 'april', 'name': 'bhanu', 'name1': 'bhanu'}

a={"idnos":[10,20,30],"names":["bhanu","gayathri","pooja","sundari"]}
a
{'idnos': [10, 20, 30], 'names': ['bhanu', 'gayathri', 'pooja', 'sundari']}
type(a)
<class 'dict'>
a.keys()
dict_keys(['idnos', 'names'])
a.values()
dict_values([[10, 20, 30], ['bhanu', 'gayathri', 'pooja', 'sundari']])
a.items()
dict_items([('idnos', [10, 20, 30]), ('names', ['bhanu', 'gayathri', 'pooja', 'sundari'])])

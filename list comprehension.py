#list comprehesion
#syntax
'''a=[expression for var in collection/range]'''

"""a=["python","java","dsa"]
a=[i.upper() for i in a]
print(a)"""

"""a=["hyd","vzg","vja"]
a=[i.capitalize() for i in a]
print(a)"""

'''a=[1,2,4,5,6,8,12,13]
b=[i*i for i in a]
print(b)'''


'''a=[1,2,4,5,6,8,12,13]
b=[i**2 for i in a]
print(b)'''


'''a=[1,2,4,5,6,8,12,13]
b=[pow(i,2) for i in a]
print(b)'''

#if-usage in list comprehension
'''a=[i for i in range(16) if i%2==0]
print(a)


a=[i**2 for i in range(16) if i%2==0]
print(a)'''

'''fruits=["apple","banana","mango","grapes","kiwi","berry"]
a=[i for i in fruits if 'a' in i ]
print(a)'''


'''fruits=["apple","banana","mango","grapes","kiwi","berry"]
a=[i for i in fruits if 'a' not in i ]
print(a)'''

#if-else usage in list comprehension

'''a=[i**2 if i%2==0 else i*5 for i in range(21)]
print(a)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[(a[i]+b[i]) for i in range(5)]
print(c)'''

'''a=[1,2,3,4,5]
b=[5,4,3,2,1]
c=[(a[i]+b[i]) for i in range(len(a))]
print(c)'''


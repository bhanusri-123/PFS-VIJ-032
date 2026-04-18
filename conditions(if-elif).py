#if-elif conditions by using comparison operators

'''a = 2
b = 4
if a<b:
    print("less")
elif b>a:
    print("greater")'''

'''a = 2
b = 4
if a==b:
    print("Equal")
elif b>a:
    print("Greater")'''

'''a = 9
b = 12
if a==b:
    print("Equal")
elif b<a:
    print("Less")
elif a!=b:
    print("Not equal")'''

#if-elif conditions by using logical operators

'''a = 2
b = 4
if a<b and b<a:
    print("Less")
elif b<a or a>b:
    print("Greater")
elif not a==b or a<b:
    print("True")'''

#if-elif conditions by using identity operators

'''a = 10.5
if type(a) is int:
    print("Integer")
elif type(a) is not float:
    print("Not float")
elif type(a) is float:
    print("Float")'''

#if-elif conditions by using membership operators

'''a = [10,20,40,56,27,33]
if 47 in a:
    print("47 in a")
elif 56 not in a:
    print("56 not in a")
elif 40 in a:
    print("40 in a")'''

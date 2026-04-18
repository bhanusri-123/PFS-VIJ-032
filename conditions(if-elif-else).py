#if-elif-else conditions by using comparison operators

'''a = 8
b = 9
if a<b:
    print("Less")
elif b>a:
    print("Greater")
elif a!=b:
    print("Not equal")
else:
    print("True")'''

#if-elif-else conditions by using logical operators

'''a = 9
b = 12
if a<b and b==a:
    print("True")
elif a!=b and a>b:
    print("or")
elif not (a==b or b>a):
    print("Not")
else:
    print("False")'''

#if-elif-else conditions by using identity operators

'''a = 8+1j
if type(a) is float:
    print("Float")
elif type(a) is int:
    print("Integer")
else:
    print("Complex")'''

#if-elif-else conditions by using membership operators

'''a = [99,33,56,23,58,45,90]
if 78 in a:
    print("78 in a")
elif 56 not in a:
    print("56 not in a")
elif 90 in a:
    print("90 in a")
else:
    print("False")'''

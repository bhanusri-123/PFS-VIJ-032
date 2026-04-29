#FUNCTIONS
# A function is a block of organized, re-usable code that is used to perform a single or multiple tasks.
# Python gives in-built functions like print,etc. You can make your own function also, which are called User-defined functions.
# A function block begins with the keyword def() followed by the function_name and paranthesis (()).

'''a = 100
b = 400
print("The sum is ",a+b)
print("The difference is ",a-b)
print("The product is ",a*b)
a = 30
b = 50
print("The sum is ",a+b)
print("The difference is ",a-b)
print("The product is ",a*b)'''

#We can simplify this process by using functions

'''def calculate(a,b):
    print("The sum is ",a+b)
    print("The difference is ",a-b)
    print("The product is ",a*b)
calculate(100,200)
calculate(30,50)
calculate(60,900)'''

'''def calculate(a,b):
    print("Integer Division",a//b)
    print("Power",a**b)
    print("Modulus",a%b)
calculate(21,7)
calculate(54,7)'''

'''def cal():
    a = int(input())
    b = int(input())
    print(a+b)
    print(a-b)
    print(a*b)
cal()'''

'''def fullname():
    fname = input("FirstName: ")
    lname = input("LastName: ")
    print((fname+" "+lname).title())
fullname()'''

#print vs return
#print just shows the human user output in a console.
#return is a keyword which is used to terminate the function and gives back a value from the function.

'''def sub(a,b):
    print(a-b)
sub(9,8)'''

'''def sub(a,b):
    return a-b
print(sub(4,1))'''

'''def cal():
    c = a+b
    d = a-b
    e = a*b
    print(c)
    print(d)
    print(e)
cal(3,5)'''

'''def cal(a,b):
    c = a+b
    d = a-b
    e = a*b
    return c
    return d
    return e
print(cal(2,3))'''

'''def cal(a,b):
    c = a+b
    d = a-b
    e = a*b
    return c,d,e
print(cal(2,3))'''

#Split Bill

'''def splitbill():
    count = int(input("Number of friends: "))
    bill = int(input("Total amount: "))
    return bill/count
print(splitbill())'''

'''def splitbill():
    count = int(input("Number of friends: "))
    bill = int(input("Total amount: "))
    amt = bill/count
    print(f"Each friend needs to pay {amt}")
splitbill()'''

'''def splitbill():
    count = int(input("Number of friends: "))
    bill = int(input("Total amount: "))
    amt = bill/count
    print("Each friend needs to pay {}".format(amt))
splitbill()'''

'''def splitbill():
    count = int(input("Number of friends: "))
    bill = int(input("Total amount: "))
    print("Each friend needs to pay {}".format(bill/count))
splitbill()'''

'''def splitbill():
    count = int(input("Number of friends: "))
    bill = int(input("Total amount: "))
    print(f"Each friend needs to pay {bill/count}")
splitbill()'''

#task-2

'''while True:
    def calculate():
        a = int(input("a value: "))
        b = int(input("b value: "))
        option = int(input("Options: 1.Addition 2.Subtraction 3.Multiplication "))
        if option==1:
            return a+b
        elif option==2:
            return a-b
        else:
            return a*b
    print(calculate())'''

'''def add():
    print(a+b)
def sub():
    print(a-b)
def mul():
    print(a*b)
while True:
    a = int(input("a value: "))
    b = int(input("b value: "))
    option = int(input("Options: 1.Addition 2.Subtraction 3.Multiplication "))
    if option==1:
        add()
    elif option==2:
        sub()
    else:
        mul()'''


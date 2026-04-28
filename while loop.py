#WHILE LOOP - continuous iteration
'''a = 10
while a<1:
    print(a)'''

'''a = 10
while a>1:
    print("True")'''

'''a = 10
while a>1:
    print(a)'''

'''a = 10
while a>=1:
    print(a)
    a = a-1 '''

'''a = 20
while a>5:
    a = a-1
    print(a)'''

'''a = 20
while a>5:
    print(a)
    a = a-1'''

'''a = 10
while a<30:
    a+=1
    print(a)'''

'''a = 10
while a>30:
    print(a)
    a+=1'''

#VOTING TASK

'''while True:
    age = int(input("Enter age: "))
    if age>=18:
        print("Eligible to vote")
    else:
        print("Not eligible to vote")'''

#EVEN OR ODD

'''while True:
    num = int(input("Enter number: "))
    if num%2==0:
        print("Even")
    else:
        print("False")'''

#LEAP YEAR

'''while True:
    year = int(input("Enter year: "))
    if year%4==0:
        print("Leap year")
    else:
        print("Not a leap year")'''


#VOWELS

'''while True:
    a = input("Enter the letter: ")
    if a in "aeiou":
        print("Vowel")
    else:
        print("Consonant")'''

'''a = [1,4,6,7,8,2,8,9,2,2,11,2]

for i in range(4):
    a.remove(2)

print(len(a))'''

#RANGE() - The range function returns a sequence of numbers by default and increments one by
#one and stops before a specific number
#start-stop-step

'''for i in range(5):
    print(i)'''
    
'''for i in range(5,15):
    print(i)'''

'''for i in range(0,20,2):
    print(i)'''

'''for i in range(0,46,5):
    print(i)'''

'''for i in range(0,28,3):
    print(i)'''


'''a = [1,4,6,7,8,2,8,9,2,2,11,2]

val = int(input("Enter value to remove: "))
k = int(input("How many times to remove: "))

count = 0
a = [x for x in a if not (x == val and (count := count + 1) <= k)]

print("Sum:", sum(a))
print("Count:", len(a))'''



# STUDENT MARKS

'''while True:
    marks=int(input("Enter marks: "))
    if marks in range(91,101):
        print("Grade A")
    elif marks in range(81,91):
        print("Grade B")
    elif marks in range(71,81):
        print("Grade C")
    elif marks in range(61,71):
        print("Grade D")
    else:
        print("Fail")'''


#Difference between break, continue, and pass
# The break statement is used to terminate the entire loop.
# The continue statement is used to skip the current iteration and rest of the code will continue.
# A pass is a null statement, it does nothing but syntactically we need.

#BREAK

'''a = 10
while a>1:
    print(a)
    a = a-1
    if a==5:
        break'''

'''a = 10
while a>1:
    a = a-1
    if a==5:
        break
    print(a)'''

'''for i in range(20):
    if i==14:
        break
    print(i)'''

'''a = "python"
for i in a:
    if i=='t':
        break
    print(i)'''

#CONTINUE

'''a = 30
while a>5:
    print(a)
    a = a-1
    if a==20:
        continue'''

'''a = 30
while a>5:
    a = a-1
    if a==20:
        continue
    print(a)'''

'''for i in range(15):
    if i==9:
        continue
    print(i)'''

'''a = "python"
for i in a:
    if i=='t':
        continue
    print(i)'''

#PASS

'''a = 40
while a>10:
    print(a)
    a = a-1
    if a==15:
        pass'''

'''for i in range(40):
    if i==10:
        pass
    print(i)'''



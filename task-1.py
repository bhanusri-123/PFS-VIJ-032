#VOTING
'''age = int(input("Enter age: "))
if age>=18:
    print("They are eligible to vote")
else:
    print("They are not eligible to vote")'''

#EVEN OR ODD
'''number = int(input("Enter a number: "))
if number%2==0:
    print("Even")
else:
    print("Odd")'''

#LEAP YEAR
'''year = int(input("Enter year: "))
if year%4==0:
    print("Leap year")
else:
    print("Not a leap year")'''

#VOWELS
'''vowels = ['a','e','i','o','u']
letter = input("Enter letter: ")
if letter in vowels:
    print("It is vowel")
else:
    print("It is consonant")'''

'''a = input("Enter the letter: ")
if a in "aeiou":
    print("Vowel")
else:
    print("Consonant")'''

'''vowels = ['a','e','i','o','u']
letter = input("Enter letter: ").lower()
if letter in vowels:
    print("It is vowel")
else:
    print("It is consonant")'''
    

#GUEST CODE
'''name = input("Enter name: ")
if guest=='Bhanusri':
    print("Welcome Bhanusri")
else:
    print("Welcome Guest")'''

'''name = input("Enter name: ").lower()
if name=='bhanusri':
    print("Welcome", name)
else:
    print("Welcome guest")'''

'''names = ["gayathri", "sarvani", "tripura", "pooja", "amrutha"]
a = input("Ennter name: ")
if a in names:
    print("Welcome", a)
else:
    print("Welcome guest")'''

#SOCIAL MEDIA LOGIN
#nested if and if-else
#username=pooja, password=1234 -> Login successful otherwise Invalid Credentials

'''username = input("Enter username: ")
password = int(input("Enter password: "))
if username=='pooja' and password==1234:
    print("Login Successful")
else:
    print("Invalid Credentials")'''


'''username = input("Enter username: ")
password = int(input("Enter password: "))
if username=="pooja":
    if password==1234:
        print("Login Successful")
    else:
        print("Invalid Credentials")'''

#BAKERY
# cake price 1200 ->redvelvet cake
#1000->Choco almond
#800->chocolate cake
#600->butterscotch
#Remaining prices-> cake is not available

'''price = int(input("Enter price: "))
if price==2000:
    print("Red Velvet Cake")
elif price==1000:
    print("Choco Almond Cake")
elif price==800:
    print("Chocolate Cake")
elif price==600:
    print("Butterscotch Cake")
else:
    print("Cake is not available")'''

#Pizza
'''pizza = input("Enter pizza name: ")
if pizza=='BBQ Pizza':
    print(1000)
elif pizza=='Crispy Chicken Pizza':
    print(800)
elif pizza=='Paneer Pizza':
    print(600)
elif pizza=='Corn Pizza':
    print(400)
elif pizza=='French fries & coke':
    print(200)
else:
    print("Pizza not available")'''

#Students mark grade system

'''marks = int(input("Enter marks: "))
if marks>=91 and marks<=100:
    print("Grade A")
elif marks>=81 and marks<=90:
    print("Grade B")
elif marks>=71 and marks<=80:
    print("Grade C")
elif marks>=50 and marks<=70:
    print("Grade D")
else:
    print("Fail")'''


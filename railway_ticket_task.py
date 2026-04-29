while True:
    def ticket_price():
        gender = input('enter your gender: ')
        age = int(input('enter your age: '))
        if gender=="male" and age>=60:
            price=1000*(30/100)
            price=1000-price
            print(price)
        elif gender=="male" and age<60:
            print(1000)
        elif gender=='female' and age>=60:
            price=1000*(50/100)
            price=1000-price
            print(price)
        elif gender=='female' and age<60:
            price=1000*(30/100)
            price=1000-price
            print(price)
    ticket_price()

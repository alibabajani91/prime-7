def number_check(number):
    c_2 = number % 2
    c_3 = number % 3
    c_5 = number % 5
    c_7 = number % 7
    c_11 = number % 11
    if number == 3 or number == 2 or number == 5 or number == 7 or number == 11:
        print(f"{number} is a prime number")
    elif number == 1:
        print("not defined")
    elif c_2 == 0 or c_3 == 0 or c_5 == 0 or c_7 == 0 or c_11 == 0:
        print(f"{number} is a complex number")
    else:
        print(f"{number} is a prime number")



def some_number():
    try:
        number_1 = int(input("enter number 1:"))
        number_2 = int(input("enter number 2:"))
        if number_1 > number_2:
            print("number 1 must be smaller than number 2")
        else:
            i = number_1
            number_check(i)
            while i < number_2:
                i += 1
                number_check(i)
    except ValueError:
        print("enter a number,not text")


def one_number():
    try:
        number_entry = int(input("enter a number:"))
        number_check(number_entry)
    except ValueError:
        print("enter a number,not text")


while True:
    cmd = input("enter your command:")
    if cmd == "some numbers":
        some_number()
    elif cmd == "one number":
        one_number()
    else:
        print("this command not defined, or maybe you write it wrong!")
def number_check(number):
    c_2 = number % 2
    c_3 = number % 3
    c_5 = number % 5
    c_7 = number % 7
    c_11 = number % 11
    if number == 3 or number == 2 or number == 5 or number == 7 or number == 11:
        return 1
    elif number == 1:
        return 2
    elif c_2 == 0 or c_3 == 0 or c_5 == 0 or c_7 == 0 or c_11 == 0:
        return 0
    else:
        return 1



def some_number():
    try:
        number_1 = int(input("enter number 1:"))
        number_2 = int(input("enter number 2:"))
        if number_1 > number_2:
            print("number 1 must be smaller than number 2")
        else:
            i = number_1
            while i < number_2:
                i += 1
                result = number_check(i)
                if result == 1 :
                    print(f"{i} = prime")
                elif result == 2:
                    print("not define")
                else:
                    print(f"{i} = complex")
    except ValueError:
        print("enter a number,not text")


def one_number():
    try:
        
        number_entry = int(input("enter a number:"))
        result = number_check(number_entry)
        if result == 1 :
            print(f"{number_entry} = prime")
        elif result == 2:
            print("not define")
        else:
            print(f"{number_entry} = complex")
    except ValueError:
        print("enter a number,not text")


while True:
    cmd = input("enter your command:")
    if cmd == "some numbers":
        some_number()
    elif cmd == "one number":
        one_number()
    elif cmd == exit:
        exit()
    elif cmd == "help":
        with open("readme.txt", "r") as f:
            print(f.read())
    else:
        print("this command not defined, or maybe you write it wrong!")
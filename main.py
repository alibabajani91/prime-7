def number_check(number_entry):
    c_2 = number_entry % 2
    c_3 = number_entry % 3
    c_5 = number_entry % 5
    c_7 = number_entry % 7
    c_11 = number_entry % 11
    if number_entry == 3 or number_entry == 2 or number_entry == 5 or number_entry == 7 or number_entry == 11:
        print(f"{number_entry} is a prime number")
    if number_entry == 1:
        print("not defined")
    if c_2 == 0 or c_3 == 0 or c_5 == 0 or c_7 == 0 or c_11 == 0:
        print(f"{number_entry} is a complex number")
    else:
        print(f"{number_entry} is a prime number")


while True:
    try:
        number_entry = int(input("enter a number:"))
        number_check(number_entry)
    except ValueError:
        print("enter a number,not text")
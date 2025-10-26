def number_check(number):
    c_2 = number % 2
    c_3 = number % 3
    c_5 = number % 5
    c_7 = number % 7
    c_11 = number % 11
    if c_2 == 0 or c_3 == 0 or c_5 == 0 or c_7 == 0 or c_11 == 0:
        print(f"the {number} number is a complex number")
    else:
        print(f"the {number} number is a prime number")

while True:
    try:
        number_entry = int(input("enter a number:"))
    except:
        print("enter a number please, not text")
    if number_entry == any:
        number_check(number_entry)


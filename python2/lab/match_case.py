# 5.	Write a Python program using match-case to take an input for a day number (1-7) 
# and print the corresponding day of the week.
# day = int(input("Enter a day(1-7)"))
day = int(input("Enter a day(1-7)"))

match day:
    case  1|'s' | 'S':
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case _:
        print("Invalid day")
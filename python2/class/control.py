#nested if...
#age = int(input("Enter your age"))
# if age >= 18:
#     if age >=80:
#         print("hlo senior citizen.", end=' ')
#     print("You can vote")
# else:
#     print("You can't vote")


# # if.... elif(i.e same as else if).....
# age = int(input("Enter your age"))
# if age >= 18:
#     if age >=80:
#         print("hlo senior citizen.", end=' ')
#     elif 79 >= age >= 40:# elif age >= 40: 
#         print("you are in your 40-79 range")
#     else:
#         print("you are less than 40")
#     print("You can vote")
# else:
#     print("You can't vote")

# # match-case statement(i.e same as switch case)
# day = (input("Enter the day no"))#int(input("Enter the day no"))
# match day:
#     case 's'|'S':
#         print("Sunday")
#     case 'm'|'M':   
#         print("monday")
#     case 3:
#         print("tuesday")
#     case _:
#         print("Days out of range")

# ternary operator using if else
age = int(input("Enter your age"))
# if age >= 18:
#     print("You can vote")
# else:
#     print("you can't vote")
result = "you can vote" if age>=18 else "you can't vote"
print(result)
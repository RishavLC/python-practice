# # 11.	Implement a Python program that generates and prints the Fibonacci sequence up to a 
# # specified number using a while loop.
# num = int(input("Enter a number:"))
# if num == 1:
#     print("0    ")
# elif num == 2:
#     print("0    1    ")
# else:
#     a, b = 0, 1
#     print(a,"   ",b,"   ")
#     for i in range(2,num):
#         c = a+b
#         a = b
#         b = c
#         print(c," ")
num = int(input("Enter a number: "))
if num <= 0:
    print("Please enter a positive integer.")
elif num == 1:
    print("Fibonacci sequence up to", num, "is: 0")
else:
    print("Fibonacci sequence up to", num, "is:")
    a, b = 0, 1
    print(a, end="   ")
    print(b, end="   ")
    count = 2
    while count < num:
        c = a + b
        print(c, end="   ")
        a = b
        b = c
        count += 1

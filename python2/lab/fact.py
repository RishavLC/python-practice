# 10.	Write a Python program to calculate the factorial of a number using a while loop.
num = int(input("Enter a number:"))
i = 1
fact = 1
while(i<=num):
    fact = fact * i
    i = i + 1
print("The factorial of number",num,"is",fact)
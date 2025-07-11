# 9.	Write a Python program to print the multiplication table of a number using a for loop.
num = int(input("Enter a number for multiplication table:"))
print("The multiplication table of:",num)
for i in range(1,11):
    print(num, "x", i, "=", num * i)
# 14.	Write a Python program that uses a for loop to iterate through numbers 1 to 20. 
# Break the loop when a number divisible by 7 is found.
for i in range(1, 21):
    print(i, end=" ")
    if i % 7 == 0:
        print("no divisible by 7 is found now exiting loop")
        break
# 13.	Create a program that uses a while loop to check if a number is prime. 
# Use the else clause to confirm it is prime.

num = int(input("Enter a No:"))
if num == 0 | num == 1:
    print(num,"is neither prime nor composite number")
else:
    i = 2
    # while i * i <= num:
    while i < num:
        if num % i == 0:
            print(num,"is not a prime number")
            break
        i += 1
    else:
        print(num,"is a prime number")
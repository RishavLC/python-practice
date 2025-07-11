# 15.	Create a program that skips numbers divisible by 3 from 1 to 15 
# using the continue statement inside a loop.
for i in range(1,16):
    if i % 3 == 0:
        continue
    print(i, end=" ") 
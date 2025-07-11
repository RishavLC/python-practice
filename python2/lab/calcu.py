# 6.	Implement a simple calculator using match-case to perform addition, subtraction,
# multiplication,and division based on user input.
num1 = int(input("Enter first no:"))
num2 = int(input("Enter second no:"))
operator = input("Enter a operator:")
match operator:
    case "+":
        print("sum:",num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Not divisible by 0")
    case _:
        print("Invalid operator")
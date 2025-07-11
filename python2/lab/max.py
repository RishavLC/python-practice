# 7.	Rewrite the following code using a ternary operator:
# if a > b: 
# 	max = a 
# else: 
# 	max = b
a = 22
b = 34
# status = ("Max is a",a) if a>b else ("max is b",b)
# print(status)
max = a if a > b else b
print(max)

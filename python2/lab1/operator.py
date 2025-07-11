# # # # if(n is len(my_list)>10):
# # # #     print(f"list is too long ({n})")

# my_list = {1,2,3,4}
# # # len_list = len(my_list)
# # # print(len_list)

# # # # if(len_list > 3):
# # # #     print("the collection is too big", len_list)

# # walrus operator (:=)
# if(size_list := len(my_list) > 3):#calculation with assignment(ie compare and store)
#     print("the collection is too big", size_list)

# # # #identity operator
# a = {1,2,3}
# b = a
# print(a is b) #True
# print(id(a))
# print(id(b)) #same id as a

# a = {1,2,3}
# b = {1,2,3}
# print(a is not b) #True
# print(id(a))
# print(id(b)) #different from a

# # membership operator

# names = ["Rishav","Lisa","Risali"]

# if "Rishav" in names:
#     print("Rishav is in the names")

# if "lalisa" not in names:
#     print("Lalisa is not in the names")

# # # chained comparison

# # # num = 11
# # # if num >=10:
# # #     if num <20:
# # #         print("num is in range of 10 and 20")
# #     # else:
# #     # print("num is not in range of 10 and 20")

# num = 10
# if 10<= num <=20:
#     print("num is in range of 10 and 20")
# else:
#     print("num is not in range of 10 and 20")

# # #Ternary operator
# # # num = 15
# # # if num%2 == 0:
# # #     print("num is even")
# # # else:
# # #     print("num is odd")

# num = 5
# status = "Even" if num%2 == 0 else "Odd"
# print(status) 



# # # f-string
# val = 'abc'
# print(f"{val} is the value from the variable val.")


name = 'Rishav'
age = 21
abc = f"""
Hello, My name is {name}
Im {age} years old.
gfh hgghgfg
dfsdf"""
print(abc)
# # for and for...else
# for i in (range(10,15)):
#     if i == 13:
#         break
#     print(i)
# else:
#     print("for loop completed sucessfully")

names = ["Rishav","Lirisa","Lisa"]

# for name in names:
#     if name == "Sita":
#         print("Sita found")
#     else:
#         print("Sita not Found")

for name in names:
    if name == "Lisa":
        print("Lisa found")
        break
else:
    print("Sita not Found")

# #while and while...else
# i = 0
# while i < 10:
#     i += 1
#     if i == 5:
#         continue
#     if i == 8:
#         break
#     print(i)
# else:
#     print("while loop completed successfully")
#     print("i is now 10")

# pass stmt
# i = 0
# class Person:
#     pass
# def hello():
#     pass
#     print("hello from function")
# if i < 10:
#     pass

# print("Hello from outside")
# hello()
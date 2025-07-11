# boys = ["Rishav","Rahul","Ayush"]
# boys[0] = "Raman"
# # girls = list(("Lisa","Sita","Gita"))
# # print(type(boys))
# # print(type(girls))
# for boy in boys:
#     print(boy)
# for girl in girls:
#     print(girl)
# a concise way to create list in python is list comprehension
# numbers = [ i for i in range(1,11) if i%2==0]
# print(type(numbers))
# print(numbers)
boys = ["Rishav","Rahul","Ayush"]
# if "hari" in boys:
#     print("yes")
# else:
#     print("no")
for boy in boys:
    if boy == "Hari":
        print("Yes, Present")
        break
else:
    print("No, Absent")
    
# parenthesis is used to create tuples
names = ("Ram", "Hari")
print(type(names))

names = list(names)
print(type(names))

names[0] = "Rishav"
print(names[0])

names = tuple(names)
print(type(names))
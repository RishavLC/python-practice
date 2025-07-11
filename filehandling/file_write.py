# file=open('test.txt','w')
# file.write("this is a test file.dhffffffffgjkdfnguygujyhgih")
# file.close()
# with open("data.txt", 'w') as f:
#     f.write(input("enter name:"))
# import os
# print(os.getcwd())  

print("Enter 10 names:")
data = []
for i in range(10):
    name = input("Name: ")
    data.append(name)
print(data)

# with open("names.txt", "w") as f:
#     for i in data:
#         f.write(i + "\n")

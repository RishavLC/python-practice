# # # # 12.	Write a program to search for a number in a list using a for loop. 
# # # # Use the else clause to print a message if the number is not found.
# list = [1,2,3,4,5,6]
# search = int(input("Enter the no to search in list: "))
# for i in range(len(list)):
#     if list[i] == search:
#         print("Number is in the list")
#         break
# else:
#     print("Not in the list")       
        
numbers = {1, 2, 3, 4, 5, 6,"Ram",'s'}
search_num = "Ram"
for i in numbers:
    if i == search_num:
        print("Number is in the list")
        break
else:
    print("Number is not in the list")

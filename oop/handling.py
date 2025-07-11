# try:
#     # num = int(input("Enter a number: ")) 
#     a=2/0
# except Exception as e:
#     print("Error:",e) 
 
# try:
#     num = [2,3,4]
#     print(num[5])
# except IndexError as e:
#     print("Error:",e)  

try:
    f = open ('abc.txt','r') 
    c = f.read()
    print(c)
except IOError as e:
    print('Error: ',e)
        
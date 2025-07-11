# # file=open('testfile.txt','r')
# file=open('data.txt','r')
# content=file.readline()
# print(content)  

# read vowel only
with open("names.txt", "r") as f:
    content = f.read().lower() 
vowels = "aeiou"

for ch in content:
    if ch in vowels:
        print(ch)

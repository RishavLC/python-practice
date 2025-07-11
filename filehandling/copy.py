with open("test.txt",'r') as f:
    content = f.read()
with open("copy_test.txt",'w') as f:
    f.write(content)
    
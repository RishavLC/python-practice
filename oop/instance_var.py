class Student:
    def __init__(self, name, roll):
        self.name = name          # instance variable
        self.roll = roll          # instance variable

        print(self.name, roll)  
       

# Create two objects
s1 = Student("Alice", 101)
s2 = Student("Bob", 102)

# print(s1.name, s1.roll)  
# print(s2.name, s2.roll)  

class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
    
    def display_details(self):
        print(f"Name:{self.name} \nRoll No: {self.roll}")

s = Student("Rishav",4)
s1 = Student("Lisa",27)

s.display_details()
s1.display_details()
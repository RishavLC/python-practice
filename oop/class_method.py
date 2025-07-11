# class Student:
#     school = "Green Valley"  # class variable

#     # def __init__(self, name):
#     #     self.name = name

#     @classmethod
#     def get_school(cls):
#         return cls.school

# # Accessing class method
# print(Student.get_school())  # Output: Green Valley



class Student:
    school = "Old School"

    @classmethod
    def update_school(cls, new_name):
        cls.school = new_name  # update class-level data

Student.update_school("New School")
print(Student.school) 

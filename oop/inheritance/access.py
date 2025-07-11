class Student:
    def __init__(self):
        self.name = "John"        # public
        self._grade = "A"         # protected
        self.__password = "1234"  # private

s = Student()
print(s.name)       # ✅ works
print(s._grade)     # ⚠️ works but not recommended
print(s._Student__password) # ❌ Error: private
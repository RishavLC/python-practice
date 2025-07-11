class Parent:
    def name(self):
        print('Parent class method')

class Child(Parent):
    def childName(self):
        print('Child class Method')

c = Child()
c.name()
c.childName()

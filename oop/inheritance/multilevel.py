class Grand:
    def grand(self):
        print("Grand father")

class Father(Grand):
    def father(self):
        print("father")

class Son(Father):
    def son(self):
        print('Son')

s = Son()
s.son()
s.grand()
s.father()

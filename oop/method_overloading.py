# from multipledispatch import dispatch

# class Math:
#     @dispatch(int,str)
#     def add(n1,n2):
#         sum = n1
#         s=n2
#         print(sum,s)
        
#     @dispatch(int,int,int)
#     def add(n1,n2,n3):
#         sum = n1+n2+n3
#         print(sum)

# m = Math()
# m.add(2,'d')
# m.add(2,3,4)


# pass any number of values.
class Calculator:
    def add(self, *numbers):
        result = sum(numbers)
        print("Sum:", result)

c = Calculator()
c.add(5, 10, 98)              # Output: Sum: 15
c.add(1, 2, 3, 4, 5)      # Output: Sum: 15


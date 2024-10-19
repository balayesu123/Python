# Example1:
# # First product method.
# # Takes two argument and print their
# # product
#
#
# def product(a, b):
#     p = a * b
#     print(p)
#
#
# # Second product method
# # Takes three argument and print their
# # product
#
#
# def product(a, b, c):
#     p = a * b * c
#     print(p)
#
#
# # Uncommenting the below line shows an error
# #product(4, 5)
#
#
# # This line will call the second product method
# product(4, 5, 5)  # 100


# # Example2: Overloading(polymorphism)
# class Human:
#     def sayHello(self, name=None):
#         if name is not None:
#             print("Hello " + name)
#         else:
#             print("Hello")
# h=Human()
# h.sayHello("scott")
# h.sayHello()
#
# #output:
# # Hello scott
# # Hello

#Example3:
class Calculation:
    def add(self,a=0,b=0,c=0):
        print(a+b+c)
cal=Calculation()
cal.add()                     # 0
cal.add(10,20)           # 30
cal.add(100,200,300)   # 600

#Example1:

#Base Class
# class Calculate:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def division(self):
#         print(self.a / self.b)
#
#
# # Derived Class
# class Add(Calculate):
#     def __init__(self, a, b):
#         Calculate.__init__(self, a, b)
#
#     def add(self):
#         print("Addition:", self.a + self.b)
#         Add.division(self)
#
#
# # Derived Class
# class Subtract(Calculate):
#     def __init__(self, a, b):
#         Calculate.__init__(self, a, b)
#
#     def subtract(self):
#         print("Subtraction:", self.a - self.b)
#         Subtract.division(self)
#
#
# obj1 = Add(34, 98)
# obj2 = Subtract(45, 67)
# obj1.add()
# obj2.subtract()

#output:
# Addition: 132
# 0.3469387755102041
# Subtraction: -22
# 0.6716417910447762




#Example2:
class Parent:
     x, y = 10, 20
     def m1(self):
         print("this m1 method from class Parent")
         print(self.x+self.y)
class child1(Parent):
    a, b = 200, 100
    def m2(self):
        print("this m2 method from class child1")
        print(self.a - self.b)
        print(self.x + self.y)
class child2(Parent):
    m, n = 2, 5
    def m3(self):
        print("this m3 method from class child2")
        print(self.m*self.n)
        print(self.x + self.y)
c1Obj = child1()
c1Obj.m1()
c1Obj.m2()
c2Obj = child2()
c2Obj.m1()
c2Obj.m3()

#output:
# this m1 method from class Parent
# 30
# this m2 method from class child1
# 100
# 30
# this m1 method from class Parent
# 30
# this m3 method from class child2
# 10
# 30
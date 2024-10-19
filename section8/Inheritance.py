# Single Level Inheritance:
# #Example1:
# class A:
#      def m1(self):
#          print("this m1 method from class A")
# class B(A):
#     def m2(self):
#         print("this m2 method from class B")
#
# print("*******class A output******")
# classAObj = A()
# classAObj.m1()
# print("*******class B output******")
# classBObj = B()
# classBObj.m1()
# classBObj.m2()

# Output:
# *******class A output******
# this m1 method from class A
# *******class B output******
# this m1 method from class A
# this m2 method from class B

#Example2:
class A:
     x, y = 10, 20
     def m1(self):
         print("this m1 method from class A")
         print(self.x+self.y)
class B(A):
    a, b = 200, 100
    def m2(self):
        print("this m2 method from class B")
        print(self.a - self.b)
        print(self.x + self.y)

cbObj = B()
cbObj.m1()
cbObj.m2()

#output:
# this m1 method from class A
# 30
# this m2 method from class B
# 100
# 30
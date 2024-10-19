#Example1:
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
class C(B):
    m, n = 2, 5
    def m3(self):
        print("this m3 method from class C")
        print(self.m*self.n)
        print(self.a - self.b)
        print(self.x + self.y)
cbObj = C()
cbObj.m1()
cbObj.m2()
cbObj.m3()

#output:
# this m1 method from class A
# 30
# this m2 method from class B
# 100
# 30
# this m3 method from class C
# 10
# 100
# 30
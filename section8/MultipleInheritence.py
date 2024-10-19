#Example1:
class Parent1:
     x, y = 10, 20
     def m1(self):
         print("this m1 method from class Parent1")
         print(self.x+self.y)
class Parent2:
    a, b = 200, 100
    def m2(self):
        print("this m2 method from class Parent2")
        print(self.a - self.b)
        print(self.x + self.y)
class child1(Parent1,Parent2):
    m, n = 2, 5
    def m3(self):
        print("this m3 method from class child2")
        print(self.m*self.n)
        print(self.x + self.y)
c1Obj = child1()
c1Obj.m1()
c1Obj.m2()
c1Obj.m3()

#output:
# this m1 method from class Parent1
# 30
# this m2 method from class Parent2
# 100
# 30
# this m3 method from class child2
# 10
# 30
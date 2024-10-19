# #Example:
# class Parent:
#     def m1(self):
#         print("this m1 method from class Parent")
# class Child(Parent):
#     def m1(self):
#         print("this m1 method from class Child")
# cObj=Child()
# cObj.m1()  # this m1 method from class Child


# #Example2: super keyword:
# class Parent:
#     def m1(self):
#         print("this m1 method from class Parent")
# class Child(Parent):
#     def m1(self):
#         print("this m1 method from class Child")
#         super().m1()         # super keyword
# cObj=Child()
# cObj.m1()
# #output:
# # this m1 method from class Child
# # this m1 method from class Parent

# #Example3: Overriging the variables
# class Parent:
#     print("this m1 method from class Parent")
#     name = 'scott'
# class Child(Parent):
#     print("this m1 method from class Child")
#     name = 'john'   # this 'john' override the 'scott'
# cObj=Child()
# print(cObj.name)
#output:
# this m1 method from class Parent
# this m1 method from class Child
# john

#Example4: If variables name contains same
# accessing parent class variable through child class using super() function
class Parent:
    name = 'scott'
class Child(Parent):
    name = 'john'   # this 'john' override the 'scott'
    def Var(self):
        print(super().name)
cObj=Child()
print(cObj.name)
cObj.Var()
#output:
# john
# scott
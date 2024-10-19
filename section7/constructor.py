# class MyClass:
#     def __init__(self):           # non-parameterised constructor
#         print('this is a constructor')
# obj = MyClass()    # constructor will called automatically when object is ctreated
                  #  No need to call separately
#output:
# this is a constructure

#Example2:
# class MyClass:
#     def __init__(self):     # non-parameterised constructor
#         print('this is a constructor')
#
#     def method(self):       # method
#         print('this is a method')
#
# obj = MyClass()
# obj.method()  # method we have to call explicitely by using object.

#output

# this is a constructor
# this is a method

# #Example3:
# class MyClass:
#     name='bala'
#     def __init__(self,name):     # constructor expecting one argument
#         print(self.name)
#         print(name)
# obj = MyClass('yesu') # passing parameter to the constructor
# #output:
# bala
# yesu


#

#Example5: string type constructor it will return only string values.

# Requirement:
# class Emp:
#constructor : eid, ename, sal
#display()   : print eid, ename & sal

class Emp:
    name='bala'
    def __init__(self,eid, ename, sal):
        self.eid=eid       # converting local variables into Class variables
        self.ename=ename
        self.sal=sal
    def __str__(self):    # String type constuctor will return only strings
        return (self.ename)

obj=Emp(101,"john",50000)
print(obj)

#output:
# john











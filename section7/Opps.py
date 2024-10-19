#Example1:

# Creating a class
'''
class MyClass:
    # self parameter reference this method belongs to this class and used to access the variable of current class.
    #self is not a fixed parameter we change the self parameter name according to our convenience.
    # but it has to be the first parameter of any function in the class:
    def myfun(self):
        pass         # define function with no content, put in the pass statement to avoid getting an error.
MyClass().myfun()    # creating object

'''

#Example2:

# class MyClass:
#     def myfun1(self,name):
#         print(name)
# MyClass().myfun1("Balayesu")
# obj = MyClass()
# obj.myfun1("ABY")

#Output:
# Balayesu
# ABY

#Example#:
# class MyClass:
#     def myfun1(self,name):
#         print(name)
# MyClass().myfun1("Balayesu")
# obj = MyClass()
# obj.myfun1("ABY")

# output:
# Balayesu
# ABY

#Example3:
# class MyClass:
#     def myIns(self):
#         print("This is Instance method")
#     @staticmethod
#     def mySta():
#         print("This is static method")
# MyClass().myIns()  # Instance method (we can call only through objects)
# MyClass.mySta()    # Static method (we can directly call using class)
# MyClass().mySta()  # Static method we can call through objects also)

#Example4:
# class MyClass:
#     @staticmethod
#     def mySta(self):
#         print(self)
# MyClass.mySta("This is static method")

#Example4:
class MyClass:
    @staticmethod
    def mySta(self,name):
        print(self,name)
MyClass.mySta("Python","Static method ")


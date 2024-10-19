# class MyClass:
#     a,b = 10,20        # class variables
#     def add(self):
#         addition = self.a + self.b   # class variable access only by using 'self.variable'
#         print(addition)
# obj = MyClass()
# obj.add()

#output:
# 30

# #Example1:
#
# globalvar1 = 10         # Global Variables
# globalVar2 = 20
# class MyClass:
#     classVar1 = 50       # Class variables
#     classVar2 = 100
#     def add(self):
#         localVar1 = 2     # Local variables
#         localVar2 = 3
#
#         globalAdd = globalvar1 + globalvar1
#         classAdd = self.classVar1 + self.classVar2
#         localAdd = localVar1 + localVar2
#
#         print("Global Varaibles addition = ", globalAdd)
#         print("Class Varaibles addition = ", classAdd)
#         print("Local Varaibles addition = ", localAdd)
#
# obj = MyClass()
# obj.add()
#
# #Output:
# Global Varaibles addition =  20
# Class Varaibles addition =  150
# Local Varaibles addition =  5


#Example2: If global, class and local variable sare same.

# var1 = 10         # Global Variables
# Var2 = 20
# class MyClass:
#     Var1 = 50       # Class variables
#     Var2 = 100
#     def add(self):
#         Var1 = 2     # Local variables
#         Var2 = 3
#
#         #If variables names are same, always first preference to local variables
#         globalAdd = Var1 + Var2  # consider as local
#         classAdd = self.Var1 + self.Var2
#         localAdd = Var1 + Var2
#         accessGlobal = globals()['var1'] + globals()['Var2']
#
#         print("Global Varaibles addition = ", globalAdd)
#         print("Class Varaibles addition = ", classAdd)
#         print("Local Varaibles addition = ", localAdd)
#         print("Access Global Varaibles addition = ", accessGlobal)
#
# obj = MyClass()
# obj.add()
#
# #Output:
# Global Varaibles addition =  5
# Class Varaibles addition =  150
# Local Varaibles addition =  5
# Access Global Varaibles addition =  30

#Example3: for single class we can create multiple objects

# class MyClass:
#     def display(self,name):
#         print("This is display method...")
#         print(name)
#
# obj1 = MyClass()            # object1
# obj1.display("Bala")
#
# obj2 = MyClass()            # object2
# obj2.display("yesu")

#output:
# This is display method...
# Bala
# This is display method...
# yesu




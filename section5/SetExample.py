#Example1 : create set
# myset={'apple', 'banana', 'cherry'}
# print(myset)

#Output: {'cherry', 'banana', 'apple'}

# #Example2 : Accessing items from set
# myset={'apple', 'banana', 'cherry'}
# for i in myset:
#     print(i)
#
# #Output:
# apple
# cherry
# banana

# #Example3 : value exists in set or not
# myset={'apple', 'banana', 'cherry'}
# if 'banana1' in myset:
#     print("present")
# else:
#     print("Not present")
#
# #Output: present

#Example4 : adding items to set using add() and update()

#add() : add() methon is used to add sigle item in set
# myset={'apple', 'banana', 'cherry'}
# myset.add('orange')
# print(myset)
#Output: {'banana', 'cherry', 'apple', 'orange'}

# update() : update() is used to add multiple items to set
# myset={'apple', 'banana', 'cherry'}
# myset.update(['orange','mango', 'grapes'])
# print(myset)
#Output: {'mango', 'orange', 'apple', 'grapes', 'banana', 'cherry'}

#Example5: find the number of items from the set
# myset={'mango', 'orange', 'apple', 'grapes', 'banana', 'cherry'}
# print(len(myset))
# #output: 6

# #Example5: Remove items from the set using remove() and discard()
#
# # remove()
#
# myset={'mango', 'orange', 'apple', 'grapes', 'banana', 'cherry'}
# myset.remove('orange')
# print(myset)
# #output: {'banana', 'apple', 'mango', 'grapes', 'cherry'}
#
# # The item which is not present in the set if we try to remove it which will throw key error
# # Example:
# #myset.remove('ABC')  # KeyError: 'ABC'
#
# # discard()
# myset.discard("grapes")
# print(myset)
# #output: {'apple', 'mango', 'banana', 'cherry'}
#
# # The item which is not present in the set if we try to discard it which will not throw any error
# #Example:
# myset.discard("XYZ")
# print(myset)  # {'apple', 'mango', 'banana', 'cherry'}

# #Example6: clear all items from the set
# myset={'apple', 'banana', 'cherry'}
# myset.clear()
# print(myset)
# #output: set()
#
# del myset
# print(myset)  # NameError: name 'myset' is not defined

# #Example7: join 2 sets using union() function
# myset1={'a', 'b', 'c'}
# myset2={1,2,3}
# myset3 = myset1.union(myset2)
# print(myset3)
# #output: {1, 'c', 'a', 2, 3, 'b'}

#join 2 sets using update() function
myset1={'a', 'b', 'c'}
myset2={1,2,3}
myset1.update(myset2)
print(myset1)
#output: {'c', 1, 2, 'a', 3, 'b'}
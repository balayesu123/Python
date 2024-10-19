#Example1: creating dictionary
# mydic={'name':'bala','age':30,'sal':35}
# print(mydic)
#ouput: {'name': 'bala', 'age': 30, 'sal': 35}

#Example2: access item from the dictionary
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# print(mydic['name']) # when we pass the key that will returs value

#ouput: bala

# using get() function
# x=mydic.get('sal')
# print(x)  # 35

# #Example3: chage the value in dictionary
#
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# mydic['sal'] = 50
# print(mydic)
#
# #output: {'name': 'bala', 'age': 30, 'sal': 50}

#Example4: reading item from  dictionary using loop

# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# for i in mydic:
#     print(i)   # it captures only keys not value
#
# #output:
# # name
# # age
# # sal
#
# #Example: print only keys
#
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# for i in mydic:
#     print(mydic[i])   # it captures only values
#
# #output:
# # bala
# # 30
# # 35
#
# #Example: print only values
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# for i in mydic:
#     print(mydic.get(i))   # it captures only values
#
# #output:
# # bala
# # 30
# # 35
#
# #Example:
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# for i in mydic.values():
#     print(i)   # it captures only values

#output:
# bala
# 30
# 35

# #Example:Print keys along with value
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# for x,y in mydic.items():
#     print(x,y)   # it captures key and values
#
# #output:
# name bala
# age 30
# sal 35

# #Example5:check key is exist in dictionary or not
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# if 'name' in mydic:
#     print('exist')
# else:
#     print('not exist')
#
# #output:exist

# #Example6:cfind number of items in dictionary
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# print(len(mydic))
#
# #output: 3

# #Example7:Adding items to dictionary
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# mydic['job']='soft'
# print(mydic)
#
# #output: {'name': 'bala', 'age': 30, 'sal': 35, 'job': 'soft'}

# #Example8:remove item from dictionary
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# #pop()
# mydic.pop('age')
# print(mydic)
# #output: {'name': 'bala', 'sal': 35}
#
# #del
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# del mydic['sal']
# print(mydic)
# #output: {'name': 'bala', 'age': 30}

# #Example9:clear item from dictionary
# mydic={
#     'name':'bala',
#      'age':30,
#      'sal':35
# }
# mydic.clear()
# print(mydic)
# #output: {}

#Example9:copy  dictionary

# without using copy function
mydic={
    'name':'bala',
     'age':30,
     'sal':35
}
mydic2=mydic
print(mydic2)
#output: {'name': 'bala', 'age': 30, 'sal': 35}

# using copy function
mydic={
    'name':'bala',
     'age':30,
     'sal':35
}
mydic2=mydic.copy()
print(mydic2)
#output: {'name': 'bala', 'age': 30, 'sal': 35}







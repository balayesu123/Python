#Example1:
# myTuple = ('apple', 'orange', 'banana', 'cherry')
# print(myTuple)

#Example2: access Tuple items based on index numbers

# myTuple = ('apple', 'orange', 'banana', 'cherry')
# print(myTuple[0])  # apple
# print(myTuple[-1]) # cherry

#Example3: range of index numbers

# myTuple = ('apple', 'orange', 'banana', 'cherry', 'mango', 'banana', 'kiwi', 'lemon')
# print(myTuple[2:5])  # ('banana', 'cherry', 'mango')
# print(myTuple[-4:-1]) # ('mango', 'banana', 'kiwi')

#Example4: converting Tuple to list and list to Tuple

# myTuple = ('apple', 'orange', 'banana')
# #converting Tuple to List
# myList = list(myTuple)
# myList[2] = 'cherry'
# print(myList)            # ['apple', 'orange', 'cherry']
# #converting List to Tuple
# myTuple = tuple(myList)
# print(myTuple)           # ('apple', 'orange', 'cherry')

#Example5: readig the tuple using loop

# myTuple = ('apple', 'orange', 'banana')
#
# for i in myTuple:
#     print(i)
# Output
# apple
# orange
# banana

# #Example6: search item present in the tuple
#
# myTuple = ('apple', 'orange', 'banana')
#
# if 'orange' in myTuple:
#     print('yes, orange is present')
# else:
#     print('No, orange is not present')
#
# # Output: yes, orange is present

#Example7: find the length of tuple i.e couting  item present in the tuple

# myTuple = ('apple', 'orange', 'banana', 'cherry')
#
# print(len(myTuple))

# Output: 4

#Example8: can't add the items in the tuple

# myTuple = ('apple', 'orange', 'banana', 'cherry')
# myTuple[0] = 'orange'
# print((myTuple))

# Output: TypeError: 'tuple' object does not support item assignment

# #Example9: copy tuple
# myTuple1 = ('apple', 'orange', 'banana', 'cherry')
# myTuple2 = myTuple1
# print((myTuple1))  # ('apple', 'orange', 'banana', 'cherry')
# print((myTuple2))  # ('apple', 'orange', 'banana', 'cherry')

# #Example10: remove items from the tuple, not posible because tuple is immutable
# myTuple = ('apple', 'orange', 'banana', 'cherry')
# myTuple.remove('apple')  # invalid
# print((myTuple))
#
# # Output: AttributeError: 'tuple' object has no attribute 'remove'

# #Example11: delete all items from the tuple.
# myTuple = ('apple', 'orange', 'banana', 'cherry')
# del myTuple
# print((myTuple))
# already all items deleted from the tuple there is no value to print so that will give Name error
# Output: NameError: name 'myTuple' is not defined. Did you mean: 'tuple'?

#Example12: Join/combine tuple.
# myTuple1 = ('a','b','c','d')
# myTuple2 = (1,2,3,4)
# myTuple3 = myTuple1 + myTuple2
# print((myTuple3))

#Output: ('a', 'b', 'c', 'd', 1, 2, 3, 4)

#Example13: compare two tuples.
myTuple1 = ('a','b','c','d')
myTuple2 = (1,2,3,4)
if myTuple1 == myTuple2:
    print("tuples are equel")
else:
    print("tuples are not equel")

#Output: tuples are not equel
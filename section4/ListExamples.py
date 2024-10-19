# Example

# myList3 =  [1, "hi", "Python", 2.5]
# print(myList3)   # [1, 'hi', 'Python', 2.5]

#Example2: accessing the item from the list using index numbers

# mylist = ["apple", "banana", "cherry"]
#
# print(mylist[0])  # apple
# print(mylist[1])  # banana
# print(mylist[-1]) # cherry
# print(mylist[-2])  # banana

# #Example3: Range of indexes
#
# mylist = ["apple", "banana", "cherry","orange","kiwi","mango","lemon"]
#
# print(mylist[2:5])  # ['cherry', 'orange', 'kiwi']
# print(mylist[-1:-4])  # [] range will check from forward direction
# print(mylist[-4:-1])  # ['orange', 'kiwi', 'mango']


#Example4: change the value in list

# mylist = ["apple", "banana", "cherry"]
#
# mylist[0]="orange"
#
# print(mylist)  #  ['orange', 'banana', 'cherry']

# #Example5: Read the list items using loop
#
# mylist = ["apple", "banana", "cherry"]
#
# for i in mylist:
#     print(i)
# # Output
# apple
# banana
# cherry


#Example6: Check the item is present in the list or not

# mylist = ["apple", "banana", "cherry"]
#
# if "apple" in mylist:
#     print('apple is present')
# else:
#     print('apple is not present')

# Output : apple is present

#Example7: Find total number of items present in the list

# mylist = ["apple", "banana", "cherry"]
# print(len(mylist))

#Output : 3

#Example8: Add items into the list

# append function : append function is used to add the item at the end of the list.

# mylist = ["apple", "banana", "cherry"]
# mylist.append("orange")
# print(mylist)
#
#Output : ['apple', 'banana', 'cherry', 'orange']

#Example8: Add items into the list

# insert function: Insert function is used to add the item at any place of the list based index number.
# mylist = ["apple", "banana", "cherry"]
# mylist.insert(1,"orange")
# print(mylist)

#Output : ['apple', 'orange', 'banana', 'cherry']


#Example9: Remove items from the list

# pop function: pop function is used to remove the item from the list based index number.
# mylist = ['apple', 'orange', 'banana', 'cherry']
# mylist.pop(1)
# print(mylist)

#Output : ['apple', 'banana', 'cherry']

# del keyword: del keyword is used to remove the item from the list based index number.
# mylist = ['apple', 'orange', 'banana', 'cherry']
# del mylist[2]
# print(mylist)

#Output : ['apple', 'orange', 'cherry']


# clear() Function: clear function is used to remove all items from the list.
# mylist = ['apple', 'orange', 'banana', 'cherry']
# mylist.clear()
# print(mylist)

#Output : []  empty list

#Example10: copy items from one list to another list

# mylist1 = ['apple', 'orange', 'banana', 'cherry']
# mylist2 = list(mylist1)
# print(mylist1)
# print(mylist2)

#Output : ['apple', 'orange', 'banana', 'cherry']
 #         ['apple', 'orange', 'banana', 'cherry']


#copy() function: copy() function is used to copy items from one list to another list

# mylist1 = ['apple', 'orange', 'banana', 'cherry']
# mylist2 = mylist1.copy()
# print(mylist1)
# print(mylist2)

#Output : ['apple', 'orange', 'banana', 'cherry']
 #         ['apple', 'orange', 'banana', 'cherry']

#Example11: combine or join the list

# mylist1 = ['apple', 'orange', 'banana', 'cherry']
# mylist2 = [1,2,3,4]
# mylist3 = mylist1+mylist2  # concatenation
# print(mylist3)

#Output : ['apple', 'orange', 'banana', 'cherry', 1, 2, 3, 4]

# join two lists using looping statement

# mylist1 = ['apple', 'orange', 'banana', 'cherry']
# mylist2 = [1,2,3,4]
# for i in mylist2:
#     mylist1.append(i)
# print(mylist1)

#Output : ['apple', 'orange', 'banana', 'cherry', 1, 2, 3, 4]

# extend() function : join two lists using extend function

mylist1 = ['apple', 'orange', 'banana', 'cherry']
mylist2 = [1,2,3,4]
mylist1.extend(mylist2)

print(mylist1)
#Output : ['apple', 'orange', 'banana', 'cherry', 1, 2, 3, 4]
#Example:1
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)

# Output:
# True


#Example:2
sentence = 'The quick brown fox jumps over the lazy dog'
print('fox' in sentence)

# Output:
# True


#Example:3
numbers = ['1', '2', '3', '4', '5']
print(1 in numbers)

# Output:
# False


#Example:4
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([4, 5, 6] in nested_list)

# Output:
# True

#Example:5
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print('age' in person)

# Output:
# True

# The ‘in’ operator checks for keys in a dictionary, not values.
# If you want to check if a value is in the dictionary, you can use the values() method:

#Example:6
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print('Alice' in person)

# Output:
# False


#Example:7
person = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(25 in person.values())

# Output:
# True


# in and not in operator

S = 'Balayesu'
print('y' in S)   # True

print('y' not in S)  # False







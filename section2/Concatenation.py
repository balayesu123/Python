
# Join the numbers (same data type)
print(10+10)        # 20
print(10.5+12.0)    # 22.5
print(10+15.5)      # 25.5

# by default in python True =1 and False = 0
print(True+10)      # 11
print(False+10)     # 10
print(True+True)    # 2
print(False+False)  # 0

# Join the Strings (same data type)
print('welcome'+'pyhon') # welcomepyhon
print('100'+'python')    # 100python

# Join the numbers and Strings (different data types)
print(10.5+'pyhon')    # TypeError: unsupported operand type(s) for +: 'float' and 'str'
print(100+'python')    # TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(True+'python')     # TypeError: unsupported operand type(s) for +: 'int' and 'str'

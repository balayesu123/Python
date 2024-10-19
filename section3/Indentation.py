# Example1  valid indentation
# n=1
# if n>2:
#     print("n is greater than 2")
# else:
#     print("n is not greater than 2")

# Example2  valid indentation
# The number of spaces is up to you as a programmer, but it must be at least one.
# n=5
# if n>2:
#            print("n is greater than 2")
# else:
#     print("n is not greater than 2")


# Example3  Invalid indentation  sytax error

# n=5
# if n>2:
# print("n is greater than 2")
# else:
# print("n is not greater than 2")

# Example4  valid indentation
# Should not use the different number of spaces in the same block of code, otherwise Python will give you an error:
# n=5
# if n>2:
#     print("n is greater than 2")
#           print("n is greater than 2")
#                 print("n is greater than 2")
#     print("n is greater than 2")
# else:
#     print("n is not greater than 2")


# Example5  valid indentation
# You must use the same number of spaces in the same block of code, otherwise Python will give you an error:
# n=1
# if n>2:
#     print("n is greater than 2")
#     print("n is greater than 2")
#     print("n is greater than 2")
#     print("n is greater than 2")
# else:
#             print("n is not greater than 2")
#             print("n is not greater than 2")
#             print("n is not greater than 2")


# Example1
# In python if we writen any statement without space after any block python does not consider that statement
# belongs to the block.

n=5
if n>2:
    print("n is greater than 2")
else:
    print("n is not greater than 2")
print('End of the block')

#example1:
# print('this is starting point o0f program...')
# print('this is starting point o0f program...')
# print('this is starting point o0f program...')
#
# try:
#     print(x)
# except:
#     print("Exception Occured")
#
# print('this is ending point o0f program...')
# print('this is ending point o0f program...')
# print('this is ending point o0f program...')

#example2:
# print("start program")
# try:
#     print(10/0)
# except ZeroDivisionError:
#     print('exception handled')
# print("end program")

#example3: multiple excep blocks  try, except, else, finally

# try:
#     result = 10/0   # pass 0 or number
#     print(result)
# except ZeroDivisionError:
#     print('Thrown ZeroDivisionError exeption ')
# except SyntaxError:
#     print('Thrown SyntaxError exeption ')
# except:
#     print("Exception handled")
# else:
#     print("No exeception occured")
# finally:
#     print('always execute finally block ')

#Example: raising our own exception
def enterAge(num):
    if num<0:
        raise ValueError("Only Integers are allowed")
    if num%2 == 0:
        print('even')
    else:
        print('odd')

# checking the number is even or odd by calling function
try:
   enterAge(-1)
except ValueError:
    print("ValueError exception occured and Handled")


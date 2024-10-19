'''
# Example 1
age=int(input('Enter your age:'))
if(age>=18):
    print('Aligible for vote')
else:
    print('Not Aligible for vote')


# Example 2

if True:
    print('one')
else:
    print('zero')

# Example 3
if False:
    print('one')
else:
    print('zero')
                     '''
# Example 4
# if else single line statement
num=10
print("Given Number is Even") if num%2==0 else print("Given Number is Odd")

# Example 5
# if else single line multiple statement
num=5
{print("Hellow"),print('Python')} if num%2==0 else {print("Hi"),print("Java")}
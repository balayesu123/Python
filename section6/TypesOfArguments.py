#Example1:

def func(i,j):
    print(i,j)
func(10,20)        # Positional arguments
# output   10 20

#Example2:

def func(i,j):
    print(i,j)
func(j=10,i=20)        # keyword arguments
# output   20 10

#Example3: default values assigned to the positional arguments

def func(i,j=10):
    print(i,j)
func(10,200)  # keyword arguments
func(50)
# output
# 10 200
# 50 10

#Example3: keyword arguments

def greeting(name,greetingmsg):
    print(greetingmsg+" "+name)
greeting(name='john', greetingmsg='Hello')  # keyword arguments
greeting(greetingmsg='Hello',name='john')
# output
# Hello john
# Hello john

#Example4:
def myfun(a,b,c):
    print(a,b,c)
myfun(10,20,30)  # positional arguments  10 20 30
myfun(a=10,b=20,c=30)    # Keyword arguments     10 20 30
myfun(b=20,a=10,c=30)    # Keyword arguments     10 20 30

# Note : Positional argument must appear before any keyword arguments
myfun(10,20,c=30)  # combination if positional and keyword   10 20 30
myfun(10,b=20,c=30)   # combination if positional and keyword   10 20 30

#myfun(10,b=20,30)      #SyntaxError: positional argument follows keyword argument
# this statement is wrong because positional arguments declared after keyword argument

#myfun(10,30,b=20)  # TypeError: myfun() got multiple values for argument 'b'
# this statement is syntactically correct but 'b' value we are assigned through positional argument
# and again trying to assign with keyword arguments

# function can return two multiple values
def multiReturn(a,b):
    if a>b:
        return True
    else:
        return False

res=multiReturn(10,5)
print(res, 'a, value is greater')   # True a, value is greater

print(multiReturn(5,10), 'a, value is less')   # False a, value is less


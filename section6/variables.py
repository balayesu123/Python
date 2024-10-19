#Example1:
x= 50         # Global Variable

def sam():
    y=100      # Local Variable
    print(x)
    print(y)
sam()
#output:
50
100

# #Example2:

a=10
def demo():
    a=20
    print(a)
demo()    # 20   first priority always local variable

#Example3:

m=10
def demo():
    global m          # reinitializing Global variable inside the function using global key
    m=20
    print(m)
demo()
print(m)
#o/p
20
20

# #Example4:
m=10
def demo():
# we can't reinitializing Global variable inside the function without global key
    m=20
    print(m)
demo()
print(m)
#o/p
20
10

#Example5:

def demo():
# we can direcly declar the  Global variable inside the function using global key
     global m
     m = 100
     print(m)
demo()
print(m)
#o/p
100
100
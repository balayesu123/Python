# By default a variable declared outside of the function serves as the global variable.
x=100
y=200
def add():
    # printing a global variable
    z = x+y
    print(z)
add()

def mul():
    # The function treats it as a local variable if we don't use the global keyword.
     global x
    # modifying a global variable
     x = 50
     print(x)
mul()
print(x)
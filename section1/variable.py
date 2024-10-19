# print single variable
x=10
y=20
print(x)
print(y)

# print multiple variable
x=30
y=40
print(x,y)

# separate the variables by the comma
print(1,2,3,4,5)

# print same value for two different variables
x=50
y=x
print(x,' = memory location = ',id(x))
print(y,' = memory location = ',id(y))

# print different values for same variable
a=100
print(a,' = memory location = ',id(a))
a='balayesu'
print(a,' = memory location = ',id(a))
a=25.5
print(a,' = memory location = ',id(a))
a=True
print(a,' = memory location = ',id(a))

# assign same value for multiple variables in a sigle line
x=y=z=60
print(x,y,z)

# assign multiple values for multiple variables in a sigle line
a,b,c="balayesu",25,5.7
print(b,c,a)


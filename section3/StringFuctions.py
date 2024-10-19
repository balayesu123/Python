# strg = 'Balayesu'
# print(strg[0])   #  B
# print(strg[-1])  #  u

# fine the length of the string
# S = 'Balayesu'
# print(len(S))

#    * operator uses

# star operator used to print the string value multiple times
# print(S*3)  # BalayesuBalayesuBalayesu

# multiplication numbers using * and ** stars

# print(2*3)     # 6   --- multiplication
# Using two(**) Star Operators we can get the exponential value of any integer value
# print(2**3)    # 8   --- exponential value (two to the power of three)

# S1 = ['bala','yesu']

# print(S1)     # ['bala', 'yesu']
#
# print(*S1)    # bala yesu

# slicig
# b='HelloWorld'
# print(b[2:5])  # llo
# print(b[:5])   # Hello
# print(b[5:])   # World

# print(b[1:-1])  # elloWorl
# print(b[1:-2])  # elloWor
# print(b[1:-5])  # ello
# print(b[:-5])   # Hello

# ord() and chr() Function in Python:
# print(ord('A'))  # 65  returns the ASCII code for the character.
# print(ord('a'))  # 97
# print(ord('\\')) # 92

# print(chr(65))   # A  returns the character  represented by ASCII number
# print(chr(97))   # a
# print(chr(92))   # \

#max() and min()

# print(max('Balayesu'))  # y
# x = max("aike", "Vicky", "John")
# print(x) # aike
#
# print(min('BalayesuA'))  # A
# print(min('balayesuB'))  # B
#
# x = min("John", "Vicky", "Aike")
# print(x) # Aike
#
# x = min("john", "Vicky", "aike")
# print(x) # Vicky

#use relational operators to compare the string

# print('bala' == 'yesu')  # False
# print('bala' == 'bala')  # True
# print('free' != 'freedom')  # True
# print('arrow' > 'arron')  # True
# print('right' >= 'left')  # True
# print('teeth' < 'tee')  # False
# print('yellow' == 'fellow')  # False
# print("empy string" > "") # True

# s='Bala Yesu'
# print(s.lower())  # bala yesu
# print(s.upper())  # BALA YESU

# s=' Bala Yesu '
# print(s)          # Bala Yesu
# print(s.strip())  #Bala Yesu

# s='BalaYesu'
# print(s.isalpha())  # True
# print("Bala Yesu".isalpha())  # False
#
# print(s.isdigit())  # False
# print("123".isdigit())  # True
# print("Abc123".isdigit())  # Flase
#
# print(s.isspace())  #False
# print(" bala yesu ".isspace()) # False
# print(" ".isspace()) # True
#
# print(s.islower())  # False
# print('balayesu'.islower()) # True
#
# print(s.isupper())  # False
# print("BALAYESU".isupper()) # True
#
# print("BalaYesu".isidentifier())  # True


# s='welcome to python'
# print(s.startswith('welcome')) # True
# print(s.startswith('to')) # False
#
# print(s.endswith('python'))    # True
# print(s.endswith('welcome'))    # False


# s='welcome to python'
# print(s.find('to'))  # 8
# print(s[8])          # t
# print(s.find('bala')) # -1

# s='welcome to python'
# print('before replace :',s)  # before replace : welcome to python
#
# r=s.replace('python','Java')
# print('after replace :',r)   # after replace : welcome to Java

# s='Python,Java,.Net'
# sp=s.split(',')
# print(sp)  # ['Python', 'Java', '.Net']

# s='Python','Java','.Net'
# j="#".join(s)
# print(j)     # Python#Java#.Net
#
# s1='Python'
# J="#".join(s1)
# print(J)    # P#y#t#h#o#n

# s= "welcome to python"
# print(s.capitalize())   # Welcome to python

# s= "welcome to python"
# print(s.title())        # Welcome To Python

s= "welcome To PHYTHON"
print(s.swapcase())      # WELCOME tO phython
s1= "Welcome To Python"
print(s1.swapcase())     #  wELCOME tO pYTHON
s2= "wELCOME tO pYTHON"
print(s2.swapcase())     #  Welcome To Python
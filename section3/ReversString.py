# method one

'''
s='balayesu'
rs=""
for i in s:
    rs = i + rs
print('Revers a string :',rs)
'''

# output : useyalab

# Explanation
'''
1st  iteration:  0 index value 'b' is assigned to 'i'
s= 'balayesu'       rs = ""        i = b

rs = i + rs       concatenating 'i' value with 'rs'
rs = b + ""
rs = b            reinitialising 'rs'

2nd  iteration:   1 index value 'a' is assigned to 'i'
rs = b  --->(reinitialised value)      i = a

rs = i + rs
rs = a + b
rs = ab

3rd  iteration:  2 index value 'l' is assigned to 'i'
rs = ab  --->(reinitialised value)     i = l

rs = i + rs
rs = l + ab
rs = lab

4th  iteration:  3 index value 'a' is assigned to 'i'
rs = lab  --->(reinitialised value)   i = a

rs = i + rs
rs = a + lab
rs = alab

5th  iteration:  4 index value 'y' is assigned to 'i'
rs = alab  --->(reinitialised value)      i = y

rs = i + rs
rs = y + alab
rs = yalab

6th  iteration:   5 index value 'e' is assigned to 'i'
rs = yalab  --->(reinitialised value)      i = e

rs = i + rs
rs = e + yalab
rs = eyalab

7th  iteration:   6 index value 's' is assigned to 'i'
rs = eyalab  --->(reinitialised value)      i = s

rs = i + rs
rs = s + eyalab
rs = seyalab

8th  iteration:   7 index value 'u' is assigned to 'i'
rs = seyalab  --->(reinitialised value)     i = u

rs = i + rs
rs = u + seyalab
rs = useyalab

output:
Revers a string : useyalab

'''

# method2  using slicing operator

s='balayesu'
rev=s[::-1]                           # [start : end : incremental]
print('Revers a string :', rev)       # [0 : 0 : -1 ] if we not provide the end value it will consider all values of a give string



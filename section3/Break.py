#Example 1

#breal the loop when condition is true
# for i in range(1,11):
#     if i==6:
#         break
#     print(i)
# print('control out of the loop')


for i in range(2,4):
    for j in range(1,10):
        if i==j:
            print(i,'==',j)
            break
        print('Inner loop',j)
    print('outer loop',i)
print('control out of the loop')

#Output:
# Inner loop 1
# 2 == 2
# outer loop 2
# Inner loop 1
# Inner loop 2
# 3 == 3
# outer loop 3
# control out of the loop
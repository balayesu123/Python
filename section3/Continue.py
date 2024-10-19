#Example1
# for i in range(1,10):
#     if i%2==0:
#         continue
#     print(i,end=' ')
# print()
# print('loop ends')
#
# #Output
# 1 3 5 7 9
# loop ends

data = ['bala','salary','50000']
for sal in data:
    if sal == '50000':
        continue
    print(sal)
print("Don't know")

# Output
# bala
# salary
# Don't know
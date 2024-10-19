
# Nested loop
# for i in range(2):
#     print(i)
#     for j in range(10,13):
#         print(j)
# #Output
# 0
# 10
# 11
# 12
# 1
# 10
# 11
# 12

# Example2:
# x = [1, 2]
# y = [4, 5]
# for i in x:
#     for j in y:
#         print(i, j)
# #Output:
# 1 4
# 1 5
# 2 4
# 2 5


# Example3
# x = [1, 2]
# y = [4, 5]
# i = 0
# while i < len(x) :
#   j = 0
#   while j < len(y) :
#     print(x[i] , y[j])
#     j = j + 1
#   i = i + 1
# # #Output:
# 1 4
# 1 5
# 2 4
# 2 5


# Example4
# Running outer loop from 2 to 3

# for i in range(2, 3):
#
#     # Printing inside the outer loop
#     # Running inner loop from 1 to 10
#     for j in range(1, 11):
#         # Printing inside the inner loop
#         print(i, "*", j, "=", i * j)
#     # Printing inside the outer loop
#     print()

#Output
# 2 * 1 = 2
# 2 * 2 = 4
# 2 * 3 = 6
# 2 * 4 = 8
# 2 * 5 = 10
# 2 * 6 = 12
# 2 * 7 = 14
# 2 * 8 = 16
# 2 * 9 = 18
# 2 * 10 = 20

# Example5
i=5
while i==5:
    # Printing inside the outer loop
    # Running inner loop from 1 to 10
    for j in range(1, 11):
        # Printing inside the inner loop
        print(i, "*", j, "=", i * j)
    # Printing inside the outer loop
    i=i+1
    print()
#Output
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50
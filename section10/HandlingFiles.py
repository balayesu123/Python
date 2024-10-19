#writing Data into text file
# file = open("D:/Python/demofile.txt",'w')
# file.write("This is my 1st statement....\n")
# file.write("This is my 2nd statement....\n")
# file.write("This is my 3rd statement....\n")
# file.write("This is my 4th statement....\n")
# file.write("This is my 5th statement....")
# file.close()
# print("program completed")

# reading the data from text file
# #Example1: read all data from file
# file = open("D:/Python/demofile.txt",'r')
# print(file.read())  # read all data from file
# file.close()


#Example2: read only first line data from file
# file = open("D:/Python/demofile.txt",'r')
# print(file.readline())  # read only first line data from file
# file.close()

# Example4: appending data into text file
# file = open("D:/Python/demofile.txt",'a')
# file.write("\nThis is my 6th statement....\n")
# file.write("This is my 7th statement....\n")
# print("program completed")

#Example5:Create a new file in Python

file = open("D:/Python/myfile.txt",'x')
print("New file created")
file.close()

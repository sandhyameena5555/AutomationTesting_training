#programme no =1

# #file = open('test.txt')
#this method is use for the read the data from test.txt file by step by step
# file.read(2)
#(this is the method)
# print(file.read(2))

#read one single line for using this method.
#print line by line output using this method.
#programme=2
# print(file.readline())
# print(file.readline())
# print(file.readline())
#file.close()

#programme no =03
#this while loop condition is for print n nukmber of line

# file = open('test.txt')
# line = file.readline()
# while line!="":
#     print(line)
#     line = file.readline()
#
# file.close()

#programme no =04

file = open('test.txt')
for line in file.readlines():
    print(line)

file.close()

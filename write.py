#read all the file and store all the lines in content
#reverse the list
#write the list back to the file
# import write

with open('test.txt', 'r') as reader:
    content = reader.readlines() #['sandhya ,meena,code,python ,process ,finish']
    reversed(content) #['finish, process ,code , meena ,sandhya']
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)

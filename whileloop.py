# it =5
#
# while it>1:
#     print(it)
#     it = it-1
# print("while loop is execution is done")

# it =5
#
# while it>1:
#     if it !=2:
#         print(it)
#     it = it-1
# print("while loop is execution is done")


# it = 5
#
# while it>1:
#       if it ==3:
#           break ("this break button is break all while loop after if condition is right")
#       print(it)
#       it = it -1
#
# print("while loop is execution is done")


it =10

while it>1:
    if it == 9:
        it = it -1
        continue # if this condition is right then only it will continue other wise it skip the previous condition and proceed next

    if it ==3:
        break
    print(it)

    it = it-1

print("while loop  execution is doen")

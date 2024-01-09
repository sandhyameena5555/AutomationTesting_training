# classes are user defined bluprint or prototype
#sum , multiplication , addition , constant
# A class will have methods , class varialbles , instance varialbles , construction etc
#program =01

class calculator: # this is our class name
    num = 345 , 345 , 3456, "sandhya"
    def getdata(self):
        print("i am execution this code")

obj = calculator()   #creat object with name of class
obj.getdata()
print(obj.num)  # using the object want to print the variables


# programm 02


class calculator:
    num = 100
    # default constructor
    def __init__(self):
      print("i am called automatically when this object created")
    def GetData(self):
        print("i am execution this code")

obj = calculator()
obj.GetData()
print(obj.num)





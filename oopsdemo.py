#self keybord is mandatory for calling varable name into method
#instance and class variables have whole diffrent purpose
#constructor name should __init__
#new keybord is not required when you create object
class calculator:
    num = 100

    def __init__(self, a , b): #self object any where we can use
        self.firstname = a
        self.secondname = b
        print("i am called automatically when objct is created")

    def getData(self):
        print("i am now executing as method in class")
    def summation(self): #in python can't call the name without object self is a object
      return self.firstname + self.secondname + self.num

obj = calculator(2 , 3, )
obj.getData()
print(obj.summation())

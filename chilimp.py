#inheritance class
#you can called previous data in this class with the help of the previous class name all data
# from OopsDemo import calculator
from oopsdemo import calculator


class ChildImpl(calculator):
    num2 =200

    def __init__(self):
        calculator.__init__(self , 2 , 3)

    def getCompleteData(self):
        return self.num2 + self.num + self.summation()

obj = ChildImpl()
print(obj.getCompleteData())


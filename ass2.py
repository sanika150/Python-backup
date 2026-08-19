
class Arithmetic:
    def __init__(self):
       
        self.Value1=0
        self.Value2=0
        

    def Accept(self):
        self.Value1=int(input("Enter the first number: "))
        self.Value2=int(input("Enter the second number: "))
        
    
    def Addition(self):
        print("Addition is: ",self.Value1+self.Value2)

    def Subtraction(self):
        print("Subtraction is :",self.Value1-self.Value2)

    def Multiplication(self):
        print("Multiplication is :",self.Value1*self.Value2)

    def Division(self):
        print("Division is :",self.Value1/self.Value2)

obj1 = Arithmetic()
obj2 = Arithmetic()

print("-----------")
obj1.Accept()
obj1.Addition()
obj1.Subtraction()
obj1.Multiplication()
obj1.Division()

print("------------")
obj2.Accept()
obj2.Addition()
obj2.Subtraction()
obj2.Multiplication()
obj2.Division()



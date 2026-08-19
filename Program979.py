class Arithmetic:
    #constructor
    def __init__(self,A,B):
        self.No1 = A #Characteristics
        self.No2 = B #Characteristics

    def Addition(self): #instance method
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self): #instance method
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
def main():
    aobj = Arithmetic(11,10)
    Ret = aobj.Addition()
    print("Addition is : ",Ret)
    Ret = aobj.Substraction()
    print("Substraction is : ",Ret)

main()


class Numbers:
    ROI=10.0
    def __init__(self,value):
       self.Value=value
        

    def ChkPrime(self):
        if self.Value <= 1:
            return False
        for i in range(2,int(self.Value/2)+1):
            if self.Value % i == 0:
                return False
        return True
        
    def Factor(self):
        print("Factors:",end="")
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                print(i,end="")
            print()

    def SumFactors(self):
       total = 0
       for i in range(1,self.Value):
           if self.Value % i == 0:
               total += i
       return total
   

    def ChkPerfect(self):
        return self.SumFactors() == self.Value

   
obj1 = Numbers(6)
obj2 = Numbers(7)

print("------Number 6------")
print("Prime:",obj1.ChkPrime())
print("Perfect:",obj1.ChkPerfect())
obj1.Factor()
print("Sum of factors:",obj1.SumFactors())

print("------Number 7------")
print("Prime:",obj2.ChkPrime())
print("Perfect:",obj2.ChkPerfect())
obj2.Factor()
print("Sum of factors:",obj2.SumFactors())



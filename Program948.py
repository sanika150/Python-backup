def SumFactors(No):
    isum = 0
    for i in range(1,int((No//2)+1)):
        if ( No % i == 0):
            isum = isum + i
    return isum
            

def main():
    value = 0

    print("Enter number:")
    value = int(input())
          
    Ret = SumFactors(value)
   
    print("Sum of all factors : ",Ret)
main()

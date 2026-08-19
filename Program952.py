def SumDigit(No):
    digit = 0
    isum = 0
    while(No != 0):
        digit = No % 10
        isum = isum + digit
        No = No // 10 
    return isum
        



def main():
    No = 0
    
    print("Enter the number : ")
    No = int(input())
    Ret= SumDigit(No)
    print("Sum of digits is : ",Ret)
   
main()

def summation(Arr):     #data type of Arr consider as any
    Sum = 0
    for i in range(len(Arr)):
         Sum = Sum + Arr[i]
   
    return Sum

    
     
def main():
    size = 0
    Value =0
    Ret = 0

    print("Enter the number of elements:")
    size = int(input())

    Data = list() #create list wit 0 element

    print("Enter the elements :")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    Ret = summation(Data)
    print("Summation is :",Ret)

if __name__=="__main__":
        main()
from functools import reduce

def CheckEven(No):
    return (No % 2 == 0)

def Increment(No):
    return No+1

def Add(A,B):
    return A + B


#filter function should return bool only
def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is :",Data)
    #if we remove list it will show address
    FData = list(filter(CheckEven,Data))    #Typecast as list because we need data in list format
    print("Data after filter is :",FData)

    MData = list(map(Increment,FData))    #Typecast as list because we need data in list format
    print("Data after map is :",MData)

    RData =reduce(Add,MData)
    print("Data after reduce is :",RData)

if __name__ == "__main__":
    main()
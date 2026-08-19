def CheckEven(No):
    return (No % 2 == 0)


#filter function should return bool only
def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is :",Data)
    #if we remove list it will show address
    FData = list(filter(CheckEven,Data))    #Typecast as list because we need data in list format
    print("Data after filter is :",FData)

if __name__ == "__main__":
    main()
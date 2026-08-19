from functools import reduce


#filter function should return bool only
def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is :",Data)
    #if we remove list it will show address
    FData = list(filter((lambda No:(No % 2 == 0)),Data))    #Typecast as list because we need data in list format
    print("Data after filter is :",FData)

    MData = list(map((lambda No:No+1),FData))    #Typecast as list because we need data in list format
    print("Data after map is :",MData)

    RData =reduce((lambda A,B:A+B),MData)
    print("Data after reduce is :",RData)

if __name__ == "__main__":
    main()
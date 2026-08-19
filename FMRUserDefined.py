from functools import reduce


CheckEven=lambda No:(No % 2 == 0)
Increment= lambda No:No+1
Add=lambda A,B:A+B


def filterX(Task,Elements):
    Result = list()

    for no in Elements:
        Ret = Task(no)

        if Ret == True:
            Result.append(no)


    return Result


def main():
    Data = [11,10,15,20,22,27,30]

    print("Actual data is :",Data)
    #if we remove list it will show address
    FData = list(filterX(CheckEven,Data))    #Typecast as list because we need data in list format
    print("Data after filter is :",FData)

    MData = list(map(Increment,FData))    #Typecast as list because we need data in list format
    print("Data after map is :",MData)

    RData =reduce(Add,MData)
    print("Data after reduce is :",RData)

if __name__ == "__main__":
    main()
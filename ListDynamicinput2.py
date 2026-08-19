def main():
    size = 0
    Value =0

    print("Enter the number of elements:")
    size = int(input())

    Data = list() #create list

    print("Enter the elements :")
    for i in range(size):
        Value = int(input())
        Data.append(Value)

    Sum = 0
    for i in range(size):
         Sum = Sum + Data[i]

    print("Summation is :",Sum)
     

if __name__=="__main__":
        main()
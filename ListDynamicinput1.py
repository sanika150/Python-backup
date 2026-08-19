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

    print(Data)
     

if __name__=="__main__":
        main()
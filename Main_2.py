def Multiplication(value1, value2):
    Ans = 0   #local variable
    Ans = value1 * value2
    return Ans


def main():
    No1=0 
    No2=0
    Result = 0
    No1=int(input("Enter First No: "))
    No2=int(input("Enter Second No: "))

    Result = Multiplication(No1,No2)
    print("Multiplication is:",Result)

#starter

if __name__ == "__main__":
    main()

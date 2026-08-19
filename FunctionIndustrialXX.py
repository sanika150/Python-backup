#procedural because- def keyword in CheckEven
def CheckEven(No):
    return (No % 2 == 0)
      


def main():
    Value = 0
    Ret = False
    print("Enter number:")
    Value=int(input())

    Ret = CheckEven(Value)
    
    if (Ret == True):
        print("It is Even")
    else:
        print("It is Odd")

#Starter
if __name__ == "__main__":
    main()



#procedural because- def keyword in CheckEven
def CheckEven(No):
    if (No % 2 == 0):
        return True
    else:
        return False


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



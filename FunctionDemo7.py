#Accept: multiples parameter
#Return: 1 value
def Marvellous1(value1,value2): #positiional argument
    print("Inside marvellous1: ",value1,value2)
    return 11

def main():
    Result=None
    Result=Marvellous1("Python",21)
    print("Return value is : ",Result)

if __name__ == "__main__":
    main()
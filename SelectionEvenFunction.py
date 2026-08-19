def CheckEven(No):
    if (No % 2 == 0):
        print("It is even")
    else:
        print("It is odd")


def main():
    CheckEven(21) #positional arg
    CheckEven(No = 22) #keyword arg

if __name__ == "__main__":
    main()


#user interaction should be in main
def checkEven(No):
    if (No % 2 == 0):
        print("Even number")
    else:
        print("Odd number")

def main():
    value = 0

    print("Enter number:")
    value = int(input())
          
    checkEven(value)
    
main()

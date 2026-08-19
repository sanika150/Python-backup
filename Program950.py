def DisplayDigit(No):
    digit = 0
    while(No != 0):
        digit = digit % 10
        print(digit)
        No = No / 10 #issue


def main():
    No = 0

    print("Enter the number : ")
    No = int(input())


    DisplayDigit(No)
   
main()

def CheckPerfect(No):
    isum = 0
    for i in range(1,int((No//2)+1)):
        if ( No % i == 0):
            isum = isum + i
    return (isum == No)
            

def main():
    value = 0

    print("Enter number:")
    value = int(input())
          
    Ret = CheckPerfect(value)
    if Ret == True:
        print("It is a perfect number")
    else:
        print("It is not a perfrct number")
   
main()

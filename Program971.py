def CountCapital(Brr):
   iCount = 0

   for ch in Brr: #for each
      if(ch >= 65 and ch <= 90): #issue typeerror str to int conversion
         iCount = iCount + 1

   return iCount

   

def main():
   print("Enter String : ")
   Arr = input()

   Ret = CountCapital(Arr)
   print("Number of capital characters are : ",Ret)
   

main()

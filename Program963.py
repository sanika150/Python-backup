def Minimum(Brr):
   iMin= Brr[0]

   for i in range(len(Brr)):
      if(Brr[i]<iMin):
         iMin = Brr[i]

   return iMin


def main():
   Size = 0
   Arr = []

   print("Enter number of Elements: ")
   Size = int(input())

   print("Enter the elements : ")
   Value = 0
   for i in range(Size):
      Value = int(input())
      Arr.append(Value)
   
   print(Arr)

   Ret = Minimum(Arr)
   print("Minimum  is : ",Ret)
main()

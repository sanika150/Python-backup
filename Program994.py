print("Enter the size of Array")
size = int(input())

#int *Arr = (int *)malloc(sizeof(int)*size)
Arr = [0] * size
print("Size of array is : ",len(Arr))

print(Arr[0])
print(Arr[1])
print(Arr[2])
print(Arr[3])

#free(Arr)
#delete Arr
#Arr = Null
#System.gc()

del Arr
#Indexed
#Ordered
#Immutable
Data = bytes([65,97,98])

print(Data)  #output b'A' (binary)
print(type(Data))
print(Data[0])

#Error immutable
#Data[0]=66
print(Data[0])
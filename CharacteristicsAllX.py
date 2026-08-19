class Demo:
    No =10

    def __init__(self,A,B):
        self.Value1=A
        self.Value2=B
print("Class variable No: ",Demo.No)

obj1 = Demo(11,21)
obj2= Demo(51,101)

#print(obj1.No) #class var access by class name and obj name(Allowed)


print("Instnance variable of obj1: ",obj1.Value1,obj1.Value2)   #11,21

print("Instnance variable of obj2: ",obj2.Value1,obj2.Value2)   #51 101

obj1.Value1=15

#D\emo.No=0
obj1.No=0

print("Instnance variable of obj1: ",obj1.Value1,obj1.Value2) #15.,21
print("Instnance variable of obj2: ",obj2.Value1,obj2.Value2)

print(obj1.No)
print((obj2.No))
class Demo:
    No =10

    def _init__(self,A,B):
         self.value1=A
         self.value2=B

    def fun(self):
        print("Inside instance method",self.value1,self.value2)

    @classmethod
    def sun(cls):
        print("Inside class method sun",cls.No)

    @staticmethod
    def gun():
        print("Inside static method gun",Demo.No)

Demo.sun()
print("Class variable no:",Demo.No)

obj=Demo()

obj.fun()
print("Instance variable No :",obj.value1,obj.value2)

Demo.gun()


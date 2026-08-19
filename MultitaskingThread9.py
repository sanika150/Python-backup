import threading

def Display(No1,No2,No3):
    print("Inside Display:",No1,No2,No3)

def main():
    #using keyword parameter
    t = threading.Thread(target=Display,args=(11,21,51,)) #comma is complusory as it is tuple it will add more elements
    t.start()
    
   
if __name__=="__main__":
    main()

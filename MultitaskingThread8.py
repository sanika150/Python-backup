import threading

def Display(No):
    print("Inside Display:",No)

def main():
    #using keyword parameter
    t = threading.Thread(target=Display,args=(11,)) #comma is complusory as it is tuple it will add more elements
    t.start()
    
   
if __name__=="__main__":
    main()

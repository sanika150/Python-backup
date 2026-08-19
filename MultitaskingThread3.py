#it will display end of main before child 
import threading

def Display():    #callback function
    print("Inside Display function:",threading.get_ident()) #similar to pid it will give for thread
    for i in range(100):
        print("Inside Display")


def main():
   print("Inside main:",threading.get_ident())

   t = threading.Thread(target = Display) #create thread
   t.start()
   print("End of main")

   
if __name__=="__main__":
    main()

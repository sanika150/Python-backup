import threading

def Display():    #callback function
    for i in range(10):
        print("Inside Display:",threading.get_ident())


def main():
   print("Inside main:",threading.get_ident())

   t1= threading.Thread(target = Display) #create thread
   t1.start()
   

   t2= threading.Thread(target = Display) #create thread
   t2.start()

   t1.join()
   t2.join()
   
   print("End of main")

   
if __name__=="__main__":
    main()

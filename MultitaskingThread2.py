import threading

def Display():    #callback function
    print("Inside Display function:",threading.get_ident()) #similar to pid it will give for thread


def main():
   print("Inside main:",threading.get_ident())

   t = threading.Thread(target = Display) #create thread
   t.start()
   print("End of main")

   
if __name__=="__main__":
    main()

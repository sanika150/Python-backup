import os

def main():
    FileName=input("Enter the name of file : ")
    
    if(os.path.exists(FileName)):  #check file exist or not
        fobj = open(FileName,"r")
        #attributes
        print(fobj.name)
        print(fobj.mode)
        print(fobj.closed)
        fobj.close()
        print(fobj.closed)


    else:
        print("There is no such file")

if __name__=="__main__":
    main()
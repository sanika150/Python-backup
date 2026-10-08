import os

def main():
    FileName=input("Enter the name of file : ")
    
    if(os.path.exists(FileName)):  #check file exist or not
        fobj = open(FileName,"w")
        
        print(fobj.readable()) #it is open to read or not
        print(fobj.writable()) #it is open to write or not
        print(fobj.seekable()) #able to seek


    else:
        print("There is no such file")

if __name__=="__main__":
    main()
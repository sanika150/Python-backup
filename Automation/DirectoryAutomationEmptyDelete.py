import sys
import os

def DirectoryScanner(DirName="Marvellous"):#default arg
    Ret = False
    
    Ret = os.path.exists(DirName)
    if Ret == False:
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if Ret == False:
        print("It is not a directory")
        return
    
    

    
    for FolderName,SubFolder,FileName in os.walk(DirName):
        for fname in FileName:
            fname = os.path.join(FolderName,fname)
            print("File name : ",fname) 
            print("File size : ",os.path.getsize(fname)) #patmsooses 
            if (os.path.getsize(fname)==0): #Empty files
                os.remove(fname)

    


def main():
    Border = "-"*50
    print(Border)
    print("---------Marveloous Directory Automation----------")
    print(Border)

    if (len(sys.argv)!= 2):
        print("Inavlid number of arguments")
        print("Please specify the name of Directory")
        return          

    DirectoryScanner(sys.argv[1])

if __name__=="__main__":
    main()
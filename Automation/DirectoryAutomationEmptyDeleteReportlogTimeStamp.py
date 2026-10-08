import sys
import os
import time

def DirectoryScanner(DirName="Marvellous"):#default arg
    Border = "-"*50
    timestamp = time.ctime()
    LogFileName="Marvellous%s.log" %(timestamp)
    LogFileName = LogFileName.replace(" ","_")
    LogFileName = LogFileName.replace(":","_")

    fobj=open(LogFileName,"w")  #write mode thn create if not present
    
    fobj.write(Border+"\n")
    fobj.write("This is a log file created by marvellous automation\n")
    fobj.write("This is a Directory cleaner Script\n")
    fobj.write(Border+"\n")

    Ret = False
    
    Ret = os.path.exists(DirName)
    if Ret == False:
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirName)
    if Ret == False:
        print("It is not a directory")
        return
    
    FileCount=0
    EmptyFileCount=0

    for FolderName,SubFolder,FileName in os.walk(DirName):

        for fname in FileName:
            FileCount = FileCount + 1

            fname = os.path.join(FolderName,fname)
            
           
    
            if (os.path.getsize(fname)==0): #Empty files
                EmptyFileCount = EmptyFileCount+1
                os.remove(fname)

    
    
    fobj.write("Total files scanned : "+str(FileCount)+"\n") #int to str concatenate not possible so using timestamp
    fobj.write("Total Empty files count : "+str(EmptyFileCount)+"\n") #+ for contacetnation of string
    fobj.write("This log file is created at : "+timestamp+"\n")
    fobj.write(Border+"\n")

    fobj.close()

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

    print(Border)
    print("---------Marveloous Directory Automation----------")
    print(Border)


if __name__=="__main__":
    main()
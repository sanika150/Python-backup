import hashlib
import os

def CalculateCheckSum(FileName):
    fobj=open(FileName,"rb") #binary mode

    hobj = hashlib.md5()
    #it  read chunk by chunk
    buffer = fobj.read(1000) # it will read first 1kb data
    while (len(buffer)>0): #check upto size greater than 0 kb
        hobj.update(buffer)
        buffer = fobj.read(1000)
        

    fobj.close()

    return hobj.hexdigest()

def DirectoryWatcher(DirectoryName = "Marvellous"):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if (Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if (Ret == False):
        print("IT is not directory")
        return
    
    for FolderNme,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderNme,fname)
            CheckSum = CalculateCheckSum(fname)
            print(f"File name : {fname} Checksum : {CheckSum}")


def main():
   DirectoryWatcher()

if __name__ =="__main__":
    main()
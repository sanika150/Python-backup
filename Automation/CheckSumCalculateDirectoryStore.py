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

def FindDuplicate(DirectoryName = "Marvellous"):
    Ret = False
    Ret = os.path.exists(DirectoryName)
    if (Ret == False):
        print("There is no such directory")
        return
    
    Ret = os.path.isdir(DirectoryName)
    if (Ret == False):
        print("IT is not directory")
        return
    
    Duplicate = {} #dictionary

    for FolderNme,SubFolderName,FileName in os.walk(DirectoryName):
        for fname in FileName:
            fname = os.path.join(FolderNme,fname)
            CheckSum = CalculateCheckSum(fname)

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)  #checksum -key,filename-value
            else:
                Duplicate[CheckSum] = [fname]
    return Duplicate #return duplicate dictionary

def DisplayResult(MyDict):
    Result = list(filter(lambda x : len(x)>1,MyDict.values()))
    
    Count = 0
    for value in Result:
        for subvalue in value:
            Count = Count + 1
            print(subvalue)
        print("Value of count is : ",Count)
        Count = 0

def DeleteDuplicate(Path = "Marvellous"):
    MyDict=FindDuplicate(Path)
    Result = list(filter(lambda x : len(x)>1,MyDict.values()))
    
    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if (Count > 1 ):
                print("Deleted file : ",subvalue )
                os.remove(subvalue)
                Cnt=Cnt+1
        Count = 0

    print("Total deleted files : ",Cnt)        

def main():
   Ret = DeleteDuplicate()
   
if __name__ =="__main__":
    main()
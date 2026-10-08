import hashlib
import os
import sys
import time

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

def FindDuplicate(DirectoryName ):
    
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
                 Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum] = [fname]
        return Duplicate #return duplicate dictionary
    

def DirectoryDuplicateRemoval(Path):
    Border = "-"*50
    log=open("Log.txt","w")  #write mode thn create if not present
    
    log.write(Border+"\n")
    log.write("This is a log file created by marvellous automation\n")
    log.write("Duplicate files in directory\n")
    MyDict=FindDuplicate(Path)
    Result = list(filter(lambda x : len(x)>1,MyDict.values()))
    
    Count = 0
    Cnt = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1
            if (Count > 1 ):
                os.remove(subvalue)
                log.write(subvalue+"/n")
                Cnt=Cnt+1
        Count = 0
   
    print(Cnt)  
    log.write("Total deleted files are") 
    log.write(str(Cnt)+"\n")
    log.write(Border+"\n")
    log.close()

def main():
   start_time = time.time()
   Ret = DirectoryDuplicateRemoval(sys.argv[1])
   end_time= time.time()
   print("Execution time : ",end_time-start_time)
   
if __name__ =="__main__":
    main()
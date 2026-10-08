import hashlib

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


def main():
    Ret = CalculateCheckSum("Demo.txt")
    print("Checksum is : ",Ret)
if __name__ =="__main__":
    main()
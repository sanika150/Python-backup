def main():
    try:
        fobj=open("Hello.txt","r")
        print("file gets successfully opened")

        print("Current offset is :",fobj.tell()) 
        Data=fobj.read(6)
        print("Current offset is :",fobj.tell())

        print("Data from file is:",Data)
        fobj.close()


    except FileNotFoundError:
        print("Unable to open file as ther ie no wuch file")

    finally:
        print("End of appliction")

if __name__=="__main__":
    main()
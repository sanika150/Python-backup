def main():
    try:
        fobj=open("Hello.txt","r")
        print("file gets successfully opened")

        Data=fobj.read()

        print("Data from file is:",Data)
        fobj.close()


    except FileNotFoundError:
        print("Unable to open file as ther ie no wuch file")

    finally:
        print("End of appliction")

if __name__=="__main__":
    main()
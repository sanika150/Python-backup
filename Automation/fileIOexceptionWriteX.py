def main():
    try:
        fobj=open("Hello.txt","w")
        print("file gets successfully opened")
        fobj.write("Jay Ganesh")
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as ther ie no wuch file")

    finally:
        print("End of appliction")
        fobj.close()
if __name__=="__main__":
    main()
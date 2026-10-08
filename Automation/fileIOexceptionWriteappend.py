def main():
    try:
        fobj=open("Hello.txt","a")
        print("file gets successfully opened")
        fobj.write("Python Automation")
        
       
        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as ther ie no wuch file")

    finally:
        print("End of appliction")
        fobj.close()
if __name__=="__main__":
    main()
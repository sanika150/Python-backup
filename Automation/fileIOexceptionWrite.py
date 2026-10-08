def main():
    try:
        open("Hello.txt","w")
        print("file gets successfully opened")

    except FileNotFoundError:
        print("Unable to open file as therr is no such file")

    finally:
        print("End of appliction")

if __name__=="__main__":
    main()
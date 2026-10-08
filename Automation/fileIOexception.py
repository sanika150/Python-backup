def main():
    try:
        open("demo.txt")
        print("file gets successfully opened")

    except FileNotFoundError:
        print("Unable to open file as there no such file")

    finally:
        print("End of appliction")

if __name__=="__main__":
    main()
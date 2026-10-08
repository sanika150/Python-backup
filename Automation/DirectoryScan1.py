import os

def main():
    DirectoryName=input("Enter the name of directory : ")

    print("Contents of the directory are : ")

    for FolderName,SubFolderName,FileName in os.walk(DirectoryName):
        print("Folder name: ",FolderName)

        for subf in SubFolderName:
            print("Subfolder name: ",subf)

        for fname in FileName:
                print("Filename : ",fname)

if __name__=="__main__":
    main()

#command line input

import shutil
import sys
import os
import time
import schedule
import hashlib
import zipfile
def CreateLog(FolderName):
    Border = "-"*50
    Ret = False

    Ret = os.path.exists(FolderName)

    if Ret == True:
        Ret = os.path.isdir(FolderName)
        if Ret == False :
            print("Unable to create folder")
            return
        
    else:
        os.mkdir(FolderName)
        print("Directory for log files gets created successfully")


    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S") #instaed of replace 
    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)
    print("Log file gets created with name : ",FileName)

    fobj = open(FileName, "w")
    fobj.write(Border+"\n") #\n for new line
    fobj.write("-----Marvellous Data shield------\n")
    fobj.write("  Log created at : "+time.ctime()+"\n")
    fobj.write(Border+"\n")
   

    fobj.write("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    fobj.write(Border+"\n")
    #fobj.write("------------------End of log file----------------\n")
    fobj.write(Border+"\n")

def make_zip(folder):
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    zip_name = folder + "_" + timestamp + ".zip"
    #open the zip file
    zobj= zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED) #create zip file

    for root,Dirs,files in os.walk(folder):
        for file in files:
            full_path = os.path.join(root,file) 
            relative = os.path.relpath(full_path,folder)

            zobj.write(full_path,relative)

    zobj.close()
    return zip_name

def Calculate_hash(path):
    hobj = hashlib.md5()

    fobj = open(path, "rb")
    while True:
        data = fobj.read(1024)
        if not data:
            break
        else:
            hobj.update(data)

    fobj.close()

    return hobj.hexdigest()



def BackupFiles(Source,Destination):
   
    copied_files=[]
    CreateLog("Creating the backup folder for backup process")

    os.makedirs(Destination,exist_ok=True)#check dir is already exist or not
    
    for root, Dirs, files in os.walk(Source):
        for file in files:
            src_path = os.path.join(root,file) #root is directory

            relative = os.path.relpath(src_path,Source)
            dest_path = os.path.join(Destination,relative)

            os.makedirs(os.path.dirname(dest_path),exist_ok=True)

            #copy the files if its new
            # des file not exist thn move from src(after running it will copy only new created file to dest consider data checksum)
            if((not os.path.exists(dest_path)) or (Calculate_hash(src_path)!= Calculate_hash(dest_path))): 
                shutil.copy2(src_path,dest_path) #copy2 copy data with metadata
                copied_files.append(relative)

    return copied_files

def MarvellousDataShieldStart(Source = "Data"):
    Border = "-"*50
    BackupName = "MarvellousBackup"
    CreateLog(Source)
    print(Border)
    CreateLog("Backup process started succesfully at : ",time.ctime())
    print(Border)
    files = BackupFiles(Source,BackupName)
    
    zip_file = make_zip(BackupName)
    print(Border)
    CreateLog("Backup completed successfully ")
    CreateLog("Files copied : ",len(files))
    CreateLog("Zip files gets created : ",zip_file)




def main():
    
    Border = "-"*50
    print(Border)
    print("----------Marvellous Data Shield System-----------")
    print(Border)

    if len(sys.argv)==2:
        if(sys.argv[1] == "--h" or sys.argv[1] == "H"):
            print("This script is used to")
            print("1 : Takes auto backup at given time")
            print("2 : Backup only new and updated files")
            print("3 : Create an archive of the backup periodically")
            


        elif(sys.argv[1] == "--u" or sys.argv[1] == "U"):
            print("Use the automation script as")
            print("ScriptName.py Timeinterval SourceDirectory")
            print("Timeinterval : The time in minutes for periodic scheduling")
            print("SourceDirectory : Name of directory to be back up")
        else:
            print("Unable to procees as there is no such option")
    
            print("Please use --h or --u to get more details")
    
    #python Demo.py 5 Data
    elif len(sys.argv)==3:
        print("Inside projects logic")
        print("Time interval : ",sys.argv[1])
        print("Directory Name : ",sys.argv[2])
        
        #Apply the scheduler
        schedule.every(int(sys.argv[1])).minutes.do(MarvellousDataShieldStart,sys.argv[2])
        print(Border)
        print("Data shield System started successfully")
        print("Time interval in minutes: ",sys.argv[1])
        print("Press Ctrl + C to stop the execution")
        print(Border)
        #wait till abort
        while True:
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of command line arguments")
        print("Unable to proceed as there is no such option")
        print("Please use --h or --u to get more details")



    print(Border)
    print("----------Thank you for using our script----------")
    print(Border)


if __name__ =="__main__":
    main()
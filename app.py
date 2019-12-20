from stat import S_ISREG, ST_CTIME, ST_MODE
import os, sys, time
from datetime import datetime

def getPendingMessageDetails():
    datetimenow=datetime.utcnow().strftime('%Y%m%d%H%M%S%f')
    parentFolderPath = "F:/Parent Folder/"
    errorFolderPath="F:/Parent Folder/ErrorFiles"
    folder_list=os.listdir(parentFolderPath)

    for subfolderlist in folder_list:
        if 'ErrorFiles' !=subfolderlist:
            dir_path = parentFolderPath + subfolderlist

            # all entries in the directory w/ stats
            data = (os.path.join(dir_path, fn) for fn in os.listdir(dir_path))
            data = ((os.stat(path), path) for path in data)

            # regular files, insert creation date
            data = ((stat[ST_CTIME], path)
                    for stat, path in data if S_ISREG(stat[ST_MODE]))

            for cdate, path in sorted(data):
                a = datetime.now()
                b = datetime.fromtimestamp(cdate)
                c = a - b
                data = open(errorFolderPath+'/'+datetimenow + ".txt", "a")  # open file in append mode
                filedeatils=" Create File: "+time.ctime(cdate)+" Pending File Time(Minutes): "+ str(c)+" File Name: "+ os.path.basename(path)
                data.write(filedeatils + '\n')  # separator in file
                data.close()
                print(time.ctime(cdate), os.path.basename(path))

if __name__ == '__main__':
    getPendingMessageDetails()

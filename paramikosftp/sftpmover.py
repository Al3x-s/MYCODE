#!/usr/bin/env python3
"""Alta3 Research | RZFeeser@alta3.com
   Moving files with SFTP"""

## import paramiko so we can talk SSH
import paramiko
import os
import shutil

## where to connect to
t = paramiko.Transport("10.10.2.3", 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
t.connect(username="bender", password="alta3")

## Make an sftp connection object
sftp = paramiko.SFTPClient.from_transport(t)



# iterate across the files within directory

dest = input("where do you want to move the file exact PTD")
if not os.path.exists(dest):
    os.makedirs(dest)

def movethemfiles(xxx,tpath):
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
        if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
            xxx.put("/home/student/filestocopy/"+x, tpath+x) # move file to target location
movethemfiles(sftp, dest)


## close the connections
sftp.close() # close the connection
t.close()


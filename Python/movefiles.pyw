#! /usr/bin/env python3

import os, re, shutil

os.chdir(r'/Users/dmcgee/Dropbox/Docs/_Visual Media')
folder = os.getcwd()

for item in os.listdir():
    if os.path.isdir(item):
         dir = os.listdir(item)
         anyFolders = any(os.path.isdir(f'./{item}/{(x)}') for x in dir)
         if anyFolders == False:
             os.mkdir(f'./{item}/JPEG')
             os.mkdir(f'./{item}/RAW')
             os.mkdir(f'./{item}/MOV')
             for file in dir:
                fileType = file.split('.')[-1].upper()
                if fileType == 'JPEG' or fileType == 'JPG':
                    shutil.move(f'./{item}/{(file)}',f'./{item}/JPEG/{(file)}')
                elif fileType == "CR2":
                    shutil.move(f'./{item}/{(file)}',f'./{item}/RAW/{(file)}')
                elif fileType == "MOV":
                    shutil.move(f'./{item}/{(file)}',f'./{item}/MOV/{(file)}')
                elif fileType == 'THM':
                    os.remove(f'./{item}/{(file)}')
                else:
                    continue

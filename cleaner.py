# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 20:12:12 2020

@author: vseng
"""
import os
import shutil
path=os.getcwd()
listFolders=li2=[ f.name for f in os.scandir(path) if f.is_dir() ]
path+="\\"

for folder in listFolders:
    if folder[0]=='#':
        removePath=os.path.join(path,folder)
        shutil.rmtree(removePath)


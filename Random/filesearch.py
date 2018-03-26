#===================================================#
#Python 2: This program searches and displays files
#===================================================#

import os, glob

os.chdir("/home/bayo/Documents") #This goes to path/directory

for file in glob.glob("*.pdf"):
    print file
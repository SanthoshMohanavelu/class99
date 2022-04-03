import os
import shutil

source = input("Enter the source file.. ")
destination = input("Enter the destination file.. ")

source = source + '/'
destination = destination + '/'

list_of_files = os.listdir(source)
for file in list_of_files:
    shutil.move((source + file), destination)
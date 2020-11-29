import os
def findFile(keyword,inputdir = '.'):
    fileList = []
    fileName = [file for file in os.listdir() if keyword in file ]
    print(fileName)
keyword = input("keywords")
inputdir = input("path")
findFile(keyword,inputdir)

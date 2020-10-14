from time import *
import os as realos

# filesystem layer- nothing much, more of a bunch of functions to make file handling a
# lot easier.

def readFile(file):
  filecontents = open(file, "rt")
  print(filecontents.read())
  filecontents.close();
  
def writeFile(contents, file):
  writeTo = open(file, "at")
  writeTo.write(contents)
  writeTo.close

def deleteFile(file):
  realos.remove(file)
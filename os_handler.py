import os
import sys

# command handler for the OS

def executeCommand(command):
  if command == "test":
    print("hiya")
  if command == "ys":
    ys = input("install youngshell? y/n: ")
    
    if ys == "y":
      print("installing modules for cloning: ")
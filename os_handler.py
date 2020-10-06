import os
import sys

# command handler for the OS

def executeCommand(command):
  if command == "makeService":
    name = input("filename without .py: ")
    print("checking code can be imported...")
    try:
      importlib.import_module(name)
    except ImportError:
      print("not found, aborting...")
    try:
      print("checking init function is available..."):
      service = importlib.import_module(name)
      service.init()
    except NameError:
      print("init not found, aborting...")

    
  if command == "test":
    print("hiya")
  if command == "ys":
    ys = input("install youngshell? y/n: ")
    
    if ys == "y":
      print("installing modules for cloning: ")
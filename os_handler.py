import os
import sys

# command handler for the OS

def executeCommand(command):
  
  if command == "?":
    print("makeService = make a new system service, requires restart")
    
  if command == "makeService":
    import importlib
    name = input("filename without .py: ")
    print("checking code can be imported...")
    try:
      importlib.import_module(name)
    except ImportError:
      print("not found, aborting...")
    try:
      print("checking init function is available...")
      service = importlib.import_module(name)
      service.init()
    except AttributeError:
      print("init not found, aborting...")
    else:
      f = open("os_services.py", "a")
      f.write('core.registerService("' + name + '")')
    
  if command == "test":
    print("hiya")
    
  if command == "ys":
    ys = input("install youngshell? y/n: ")
    
    if ys == "y":
      print("installing modules for cloning: ")
      
  if command == "exit":
    sys.exit(0)
  
  #else:
  #  print("\033[1;37;41m" + " Error 1E: CommandNotFound: " + command + " \033[0m")
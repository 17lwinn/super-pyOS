import os
import sys

# command handler for the OS

def executeCommand(command):
  if command == "?":
    print("makeService = make a new system service, requires restart")
    
  elif command == "makeService":
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
    
  elif command == "test":
    print("hiya")
    
  elif command == "ys":
    ys = input("install youngshell? y/n: ")
    
    if ys == "y":
      print("installing modules for cloning: ")
      os.system("git clone https://github.com/youngchief-btw/YoungShell.git && cd YoungShell/ && bash src/Setup.sh")
      print("installed.")
  elif command == "gl":
    gl = input("install glitcxCLI? y/n: ")
    
    if gl == "y":
      print("installing: ")
      os.system("curl glitcxcli.glitch.me | bash")
      print("installed.")
  elif command == "exit":
    sys.exit(0)

import os
import sys
from time import *

def startup():
  print("Beginning startup proccedure...")
  print("Step I, check modules...")
  import importlib
  try:
    importlib.import_module("os_handler")
  except ImportError:
    print("OS_HANDLER not found, aborting...")
    sys.exit("\033[1;37;41m" + "Error 1A: OS_HANDLER NOT FOUND: \n\nThis occurs when the OS command handler could not be found, either re-download the module/OS or try moving to this folder."  + "\033[0m")
  else:
    print("\033[1;37;42m" + " OS_HANDLER found " + "\033[0m")
    try:
      importlib.import_module("main")
    except ImportError:
      print("MAIN not found, aborting...")
      sys.exit("\033[1;37;41m" + "Error 1B: MAIN NOT FOUND: \n\nThis occurs when the OS code could not be found, either re-download the module/OS or try moving to this folder."  + "\033[0m")
    else:
      print("\033[1;37;42m" + " MAIN found " + "\033[0m")
      sleep(2)


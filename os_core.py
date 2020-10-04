import os
import sys
from time import *

def startup():
  def moduleCheck():
    import importlib
    try:
      importlib.import_module("os_handler")
    except ImportError:
      print("\033[1;37;41m" + "OS_HANDLER not found, aborting...")
      sys.exit("Error 1A: OS_HANDLER NOT FOUND: \n\nThis occurs when the OS command handler could not be found, either re-download the module/OS or try moving to this folder."  + "\033[0m")
    else:
      print("\033[1;37;42m" + " OS_HANDLER found " + "\033[0m")
    try:
      importlib.import_module("main")
    except ImportError:
      print("\033[1;37;41m" + "MAIN not found, aborting...")
      sys.exit("Error 1A: MAIN NOT FOUND: \n\nThis occurs when the main OS could not be found, either re-download the module/OS or try moving to this folder."  + "\033[0m")
    else:
      print("\033[1;37;42m" + " MAIN found " + "\033[0m")
  print("Beginning startup proccedure...")
  print("Step I, Finding required modules...")
  sleep(2)
  moduleCheck()
  
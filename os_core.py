import os
import sys
from time import *

def startup():
  print("Beginning startup proccedure...")
  import importlib
  try:
    importlib.import_module("os_handle")
  except ImportError:
    print("\033[1;32;40m OS_HANDLER not found, aborting...")
    sys.exit("Error 1A: OS_HANDLER NOT FOUND: \n\n This occurs when the OS command handler could not be found, either re-download the module/OS or try moving to this folder")
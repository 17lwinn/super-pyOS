# The core module, handles the system services and more.

import os
import sys
from time import *
import traceback
import importlib

def registerService(service):
  try:
    importlib.import_module(service)
  except ModuleNotFoundError:
    print("\033[1;37;41m" + " Error 1D: ServiceNotFound: " + service + " \033[0m")
  except TypeError:
    print("\033[1;37;41m" + " Error ?: " + traceback.format_exc() + " \033[0m")
  else:  
    service = importlib.import_module(service)
    service.init()
    
def loadDrive(drive):
  try:
    os.chdir(drive)
  except OSError:
    print("\033[1;37;41m" + " Error 1F: DriveNotFound: " + drive + " \033[0m")
    
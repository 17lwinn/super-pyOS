# The core module, handles the system services and more.

import os
import sys
from time import *
import importlib

def registerService(service):
  try:
    importlib.import_module(service)
  except ModuleNotFoundError:
    print("\033[1;37;41m" + " Error 1D: ServiceNotFound: " + service + " \033[0m")
  else:  
    service = importlib.import_module(service)
    service.init()
    
def ismr(mnt):
    with open('/proc/mounts') as f:
        for line in f:
            device, mount_point, filesystem, flags, __, __ = line.split()
            flags = flags.split(',')
            if mount_point == mnt:
                return 'ro' in flags
        raise ValueError('mount "%s" doesn\'t exist' % mnt)
        
def loadDrive(drive):
  try:
    os.chdir(drive)
    if ismr(drive)==False:
      print("\033[1;37;41m" + " Error 1F-READ: Readonly: " + drive + " \033[0m")
      print("\033[1;37;41m" + " Sorry, it seems like this drive is read-only. You will not be able to do some things.." + " \033[0m")
  except OSError:
    print("\033[1;37;41m" + " Error 1F: DriveNotFound: " + drive + " \033[0m")
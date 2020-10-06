import os_handler as command
import os_core as core
import importlib
import sys
from os_services import *
import os

try:
  importlib.import_module("os_core")
except ImportError:
    print("OS_CORE not found, aborting...")
    sys.exit("\033[1;37;41m" + "Error 1C: OS_CORE NOT FOUND: \n\nThis occurs when the OS core could not be found, either re-download the module/OS or try moving to this folder."  + "\033[0m")
else:
  print("")

def main():
  com = input(os.getcwd() + "> ")
  command.executeCommand(com)

while True:
  main()
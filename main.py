import os_handler as command
import os_core as core
import importlib
import sys

try:
  importlib.import_module("os_core")
except ImportError:
    print("OS_CORE not found, aborting...")
    sys.exit("\033[1;37;41m" + "Error 1C: OS_CORE NOT FOUND: \n\nThis occurs when the OS core could not be found, either re-download the module/OS or try moving to this folder."  + "\033[0m")
else:
  print("")

core.registerService("os_handler")

com = input("> ")
command.executeCommand(com)
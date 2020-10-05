import os
import sys
from time import *
import importlib

def registerService(service):
  service = importlib.import_module(service)
  service.init()
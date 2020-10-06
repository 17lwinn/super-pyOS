import os_core as core
import os_handler as command


#reserved process ids are process ids used by the system, if a process that is being made tries to take one of these ids 
#without some sort of identification that they are from the system, the process will be ended before it could cause damage to the system 
ReservedProcessIds = range(0,3)
print(ReservedProcessIds)

class Process:
  def __init__(self, name, process, ID):
    self.name = name
    
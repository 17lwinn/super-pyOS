import os_core as core
import os_handler as command


#reserved process ids are process ids used by the system, if a process that is being made tries to take one of these ids 
#without some sort of identification that they are from the system, the process will be ended before it could cause damage to the system 
reservedProcessIds = list(range(1,5))

class process:
  name = ""
  
  def __init__(self, name, proc, ID):
    self.name = name
    for reservedId in reservedProcessIds:
      if reservedId == ID:
        del self.name
x = process("a", "b", 1)
print(x.name)
import os_handler as command
import os_core as core

core.startup()

com = input("> ")
command.executeCommand(com)

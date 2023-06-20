# BDOS Bootloader

import sys
# caution: path[0] is reserved for script path (or '' in REPL)
sys.path.insert(1, 'src\kernel')

import syscalls as sys

call = sys.System()

kern = call.find_file(filename="KERNEL.BIN")

if kern == 1:
    print("Couldn't find KERNEL.BIN!")
    quit()
else:
    call.run_os_file(kern)
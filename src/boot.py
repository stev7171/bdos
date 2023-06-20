# BDOS Bootloader

import kernel.syscalls as sysc

call = sysc.System()

kern = call.find_file(filename="KERNEL.BIN")

if kern == 1:
    print("Couldn't find KERNEL.BIN!")
    quit()
else:
    call.run_os_file(kern)
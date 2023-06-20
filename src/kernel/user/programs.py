import syscalls

def test():
    call = syscalls.System()
    call.println("Hello, World!")

def listroot():
    call = syscalls.System()
    call.listroot()
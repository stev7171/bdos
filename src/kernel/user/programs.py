import syscalls

def test():
    call = syscalls.System()
    call.println("Hello, World!")

def listroot():
    call = syscalls.System()
    call.listroot()

def cli():
    while True:
        call = syscalls.System()
        import kernel
        prompt = call.get_input("> ")

        if prompt == 'exit': quit()

        kernel.run_cmd(prompt+"//")
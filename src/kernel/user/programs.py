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
        if prompt == 'help':
            call.println("==== HELP MENU ====")
            call.println("help: brings up this menu")
            call.println("println: prints specified message (options: [RESULT])")
            call.println("input: prompts user with specified prompt (returns: [RESULT])")
            call.println("run: runs specified file (options: [RESULT], [INT])")
            call.println("listroot: lists all files that exist")

        kernel.run_cmd(prompt+"//")
# BDOS Kernel (Syscalls are in "syscalls.py")
# Version 1.0

# How to use this in your projects:
#   1. set "os" variable to True
#   2. in "os.py", make your os (you can use multiple files, but make sure your main file is "os.py")
#   3. have fun with your OS!

# Don't touch anything else unless you know what you're doing!

os = False




# Imports
import syscalls
import os as OS

call = syscalls.System()

def run(task):
    # Log the task we're running so that I don't have to figure it out myself
    print(f"Running task: {task}")

    # We don't want to run files that aren't runnables (.RUN)
    if '.RUN' in task:
        program = call.get_file_contents(task)

        # If the file exists, run it. Otherwise, throw an error
        if program != 1:
            arg_count = 0
            arg_1 = ''
            arg_2 = ''
            command = ''
            slash_count = 0

            sysret = ''

            # Iterate through the program
            for i in program:
                if i == "\\":
                    continue

                if i == '/':
                    slash_count += 1

                if slash_count == 2:

                    # Commands
                    if command == "println":
                        call.println(arg_1)
                    if command == "run":
                        call.run_bin_file(arg_1)
                    if command == "listroot":
                        call.listroot(arg_1)
                    if command == "input":
                        sysret = call.get_input(arg_1)
                    
                    # Commands with special arguments
                    if command == "println" and arg_1 == "[RESULT]":
                        call.println(sysret)
                    if command == "run" and arg_1 == "[RESULT]":
                        call.run_bin_file(sysret)

                    # Reset variables
                    arg_count = 0
                    arg_1 = ''
                    arg_2 = ''
                    command = ''
                    slash_count = 0

                # Add [i] to the command or the arguments depending on what [arg_count] is
                if i == ':': arg_count += 1
                elif arg_count == 0 and i != ':' and i != '/': command += i
                elif arg_count == 1 and i != ':' and i != '/': arg_1 += i
                elif arg_count == 2 and i != ':' and i != '/': arg_2 += i
        else:
            print("ERROR: file does not exist!")
    else:
        print("ERROR: incorrect format")

# sysret is used in run_cmd
# if it was in run_cmd, certain commands wouldn't work
sysret = ''

def run_cmd(program):
    global sysret

    arg_count = 0
    arg_1 = ''
    arg_2 = ''
    command = ''
    slash_count = 0

    for i in program:
        if i == "\\":
            continue

        if i == '/':
            slash_count += 1

        if slash_count == 2:

            # Commands
            if command == "println":
                if arg_1 == "[RESULT]": call.println(sysret)
                else: call.println(arg_1)
            if command == "run":
                if arg_1 == "[RESULT]": call.get_input(sysret)
                else: call.run_bin_file(arg_1)
            if command == "listroot":
                call.listroot(arg_1)
            if command == "input":
                sysret = call.get_input(arg_1)

            # Reset variables
            arg_count = 0
            arg_1 = ''
            arg_2 = ''
            command = ''
            slash_count = 0

        # Add [i] to the command or the arguments depending on what [arg_count] is
        if i == ':': arg_count += 1
        elif arg_count == 0 and i != ':' and i != '/': command += i
        elif arg_count == 1 and i != ':' and i != '/': arg_1 += i
        elif arg_count == 2 and i != ':' and i != '/': arg_2 += i

if __name__ == '__main__':
    if os:
        OS.start()
    else:
        call.run_bin_file("CLI.BIN")
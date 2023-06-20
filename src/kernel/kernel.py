# BDOS Kernel

# Imports
import syscalls

call = syscalls.System()

def run(task):
    # We don't want to run files that aren't runnables (.RUN)
    if '.RUN' in task:
        program = call.get_file_contents(task)

        # If the file exists, run it. Otherwise, throw an error
        if program != 1:
            arg_count = 0
            arg_1 = ''
            arg_2 = ''
            command = ''
            colon_count = 0

            sysret = ''

            # Iterate through the program
            for i in program:
                if i == "\\":
                    continue

                if i == ':':
                    colon_count += 1

                if colon_count == 2:

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
                    colon_count = 0

                # Add [i] to the command or the arguments depending on what [arg_count] is
                if i == '|': arg_count += 1
                elif arg_count == 0 and i != '|' and i != ':': command += i
                elif arg_count == 1 and i != '|' and i != ':': arg_1 += i
                elif arg_count == 2 and i != '|' and i != ':': arg_2 += i
        else:
            print("ERROR: file does not exist!")
    else:
        print("ERROR: incorrect format")


call.run_bin_file("TEST.BIN")

run("TESTAPP.RUN")
# BDOS Kernel

# Imports
import syscalls

call = syscalls.System()

def run(task):
    if '.RUN' in task:
        program = call.get_file_contents(task)

        if program != 1:
            arg_count = 0
            arg_1 = ''
            arg_2 = ''
            command = ''
            colon_count = 0

            for i in program:
                if i == "\\":
                    continue

                if i == ':':
                    colon_count += 1

                if colon_count == 2:

                    if command == "println":
                        call.println(arg_1)

                    arg_count = 0
                    arg_1 = ''
                    arg_2 = ''
                    command = ''
                    colon_count = 0

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
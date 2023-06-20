# All syscalls are in this file

# Imports
import files
import kernel
import src.os.operating_system as operating_system

class System:
    def __init__(self):
        kernel.start()

    def create_file(self, filename, file_contents):
        files.files[filename] = file_contents

    def start_os(self):
        operating_system.start()
    
    def remove_file(self, filename):
        files.files.pop(filename)
    
    def println(self, msg):
        print(f'{msg}\n')

    def get_input(self, prompt):
        input(prompt)

    def overwrite_file(self, filename, new_contents):
        if filename in files.files:
            files.files[filename] = new_contents
        else:
            print("Error: file doesn't exist")
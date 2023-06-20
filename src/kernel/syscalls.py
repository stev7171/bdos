# All syscalls are in this file

# Imports
import os
import files
import user.programs

class System:
    def create_file(self, filename, file_contents):
        files.files[filename] = file_contents
   
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
            return 1

    def find_file(self, filename):
        if filename in files.files:
            return filename
        else:
            return 1

    def run_os_file(self, filename):
        os.chdir('src/kernel')
        os.startfile(files.files[filename])

    def run_bin_file(self, filename):
        if filename in files.files:
            program = getattr(user.programs, files.files[filename])
            program()
            return 0
        else:
            return 1
    
    def get_file_contents(self, filename):
        if filename in files.files:
            return files.files[filename]
        else:
            return 1
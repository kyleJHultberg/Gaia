import os

class FileController():
    def __init__(self, dir, file_name, mode):
        
        if os.path.isdir(dir):
            self.file = open(dir + file_name, mode)
        else:
            os.mkdir(dir)
            self.file = open(dir + file_name, mode)        

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


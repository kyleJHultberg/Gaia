import os
from utilities import FileController
from body import Body



class Project(Body):
    def __init__(self, name, path_root):
        self.name = name
        self.path_root = path_root
        self.full_folder_path = path_root + name + "/"

    def createProjectFolder(self):
        os.mkdir(self.full_folder_path)

    def createFolder(self, path):
        if os.path.isdir(path):
            print(path)
            return path
        else:
            os.mkdir(path)
            return path
    
    def createFile(self, path, file_name, mode, body):
        with FileController(str(path), str(file_name), mode) as opened_file:
            opened_file.write(body)


    def createDefaultTemplate(self):
        if os.path.isdir(self.full_folder_path) == False:
            self.createProjectFolder()
        
        self.www_folder_path = self.createFolder(self.full_folder_path + "www/")
        
        self.createFile(self.full_folder_path, "main.py", "w", self.createMainDotPy())
        self.createFile(self.www_folder_path, "views.py", "w", self.createViewsDotPy())
        self.createFile(self.www_folder_path, "__init__.py", "w", self.createInitDotPy())

        self.static_folder_path = self.createFolder(self.full_folder_path + "www/static/")

        self.templates_folder_path = self.createFolder(self.full_folder_path + "www/templates/")

        self.createFile(self.templates_folder_path, "index.html", "w", self.createIndexDotHtml())

        # with FileController(str(self.full_folder_path), "main.py", "w") as opened_file:
        #     opened_file.write(self.createMainDotPy())
        # self.www_folder_path = self.createFolder(self.full_folder_path + "www/")
        # with FileController(str(self.www_folder_path), "views.py", "w") as opened_file:
        #     opened_file.write(self.createViewsDotPy())
        # with FileController(str(self.www_folder_path), "__init__.py", "w") as opened_file:
        #     opened_file.write(self.createInitDotPy())
        # with FileController(str(self.templates_folder_path), "index.html", "w") as opened_file:
        #     opened_file.write(self.createIndexDotHtml())



        
    




import os
from utilities import FileController
from body import Body


"""
Documentation:

    Everything related to the overall project should start here.

    self.name - The name of the project the user is creating.  For example,
    if someone was creating a template for a website they were creating called
    Facebook, self.name would be Facebook.

    self.path_root = The idea is to allow the user to create a template that will
    reside in the place of their choosing.  The end goal will be for a user to
    choose the filepath from a GUI.

"""


class Project(Body):
    def __init__(self, name, path_root):
        self.name = name
        self.path_root = path_root
        self.full_folder_path = path_root + name + "/"

    def createProjectFolder(self):
        os.mkdir(self.full_folder_path)

    def createDefaultTemplate(self):
        if os.path.isdir(self.full_folder_path) == False:
            self.createProjectFolder()

        self.www_folder_path = self.full_folder_path + "www/"
        os.mkdir(self.full_folder_path + "www/")

        self.static_folder_path = self.full_folder_path + "www/static"
        os.mkdir(self.full_folder_path + "www/static")

        self.templates_folder_path = self.full_folder_path + "www/templates/"
        os.mkdir(self.full_folder_path + "www/templates")

        with FileController(str(self.www_folder_path), "views.py", "w") as opened_file:
            opened_file.write(self.createViewsDotPy())

        with FileController(str(self.www_folder_path), "__init__.py", "w") as opened_file:
            opened_file.write(self.createInitDotPy())

        with FileController(str(self.templates_folder_path), "index.html", "w") as opened_file:
            opened_file.write(self.createIndexDotHtml())

        with FileController(str(self.full_folder_path), "main.py", "w") as opened_file:
            opened_file.write(self.createMainDotPy())

        
    




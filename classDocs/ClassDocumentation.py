

from fileinput import filename
from xmlrpc.client import boolean


class ClassDocumentation:
    def __init__(self,file_name,variables = False,classses = False) -> None:
        self.file_name  =  file_name
        self.variables =  variables
        self.classes = classses

    def openFile(self):
        with open(self.file_name) as file:
            lines = file.readlines()
            for i in lines:
                if
            print(lines)


    



    
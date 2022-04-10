
import re
import os


class ClassDocumentation:
    def __init__(self,file_name,variables = False,classses = False) -> None:
        self.file_name  =  file_name
        self.variables =  variables
        self.classes = classses
        self.parent_directory = "documentation"

    def openFile(self):
        with open(self.file_name) as file:
            lines = file.readlines()
            for i in lines:
                string = re.findall("\w+\s+\=\s+\d+|\w+\s+\=\s+\w+",i)
                split_string  = string[0].split("=")

                full_string = string[0] + f" #Assign {split_string[0]} to {split_string[1]}"

                if not os.path.exists(self.parent_directory):
                    os.makedirs(self.parent_directory)

                filena = self.file_name.split(".")[0] + "Documentation.py" 
                with open(os.path.join(self.parent_directory, filena ), 'a') as temp_file:
                    temp_file.write(full_string)
                    temp_file.write("\n")
                    temp_file.close()
                file.close()
            print(lines)


    



    
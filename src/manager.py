from .project import Project

import os
import glob
import shutil

class Manager:


    def __init__(self):
        print("Manager")

    # List all files in /Projects folder - assuming they are projects
    def list_all_projects(self):
        return os.listdir('../Projects/')

    # Create a new folder for a project
    def create_folder(self, directory):
        try:
            if not os.path.exists('../Projects/' + directory):
                os.makedirs('../Projects/' + directory + '/data')
                self.create_project_file(directory)
                return "New directory " + directory + " created"
            else:
                return "Directory already exists"
        except OSError:
            print('Error: Opening directory. ' + directory)

    # Create a default project.txt file
    def create_project_file(self, directory):
        f = open('../Projects/' + directory + "/project.txt", "w+")
        f.write("name="+directory+"\n")
        f.write("dnn_type=cnn"+"\n")
        f.write("download_url="+"https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"+"\n")
        f.write("data_set_name="+"\n")
        f.write("epochs=10"+"\n")
        f.write("loss_function=CategoricalCrossentropy"+"\n")
        f.write("optimizer=adam"+"\n")
        f.write("batch_size=64"+"\n")
        f.write("model_format=h5"+"\n")
        f.write("tf_lite_model=yes"+"\n")
        f.close()

    # Open specified project and return content of project.txt
    def open_project(self, directory):
        try:
            if os.path.exists('../Projects/' + directory):
                file = open('../Projects/' + directory + "/project.txt", "r")

                myvars = {}
                for line in file:
                    name, var = line.partition("=")[::2]
                    myvars[name.strip()] = str(var)

                project = Project()
                project.parse_input(myvars)
    
                return "Project file opened", project
            else:
                return "Project file could not be opened", None
        except OSError:
            print('Error: Opening directory. ' + directory)      

    # Changes made to project are saved back to project.txt
    def save_project(self, project):
        f = open('../Projects/' + project.name[:-1] + "/project.txt", "w+")
        f.write("name="+project.name +"\n")
        f.write("dnn_type="+project.dnn_type+"\n")
        f.write("download_url="+project.download_url+"\n")
        f.write("data_set_name="+project.data_set_name+ "\n")
        f.write("epochs="+project.epochs+"\n")
        f.write("loss_function="+project.loss_function+"\n")
        f.write("optimizer="+project.optimizer+"\n")
        f.write("batch_size="+project.batch_size+"\n")
        f.write("model_format="+project.model_format+"\n")
        f.write("tf_lite_model="+project.tf_lite_model+"\n")
        f.close()
        

    # Deleting a new folder for a project
    def delete_folder(self, directory):
        try:
            if os.path.exists('../Projects/' + directory):
                shutil.rmtree('../Projects/' + directory)
                return "Project file deleted"
            else:
                return "Specified directory cannot be found"
        except OSError:
            print('Error: Deleting directory. ' + directory)

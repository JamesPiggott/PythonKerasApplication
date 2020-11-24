from .project import Project

import os
import shutil


class Manager:
    def __init__(self):
        self.projects = "Projects"
        self.project_folder = os.path.join("..", self.projects)
        print("Manager")

    # List all files in Projects folder - assuming they are projects
    def list_all_projects(self):
        try:
            if os.path.exists(self.project_folder):
                return os.listdir(self.project_folder)
            else:
                print("There is no " + self.projects + " directory")
                return None
        except OSError:
            print('Error: Opening directory. ' + self.project_folder)
            return None

    # Create a new folder for a project
    def create_folder(self, directory):
        new_directory = os.path.join(self.project_folder, directory)
        data_directory = os.path.join(new_directory, "data")
        try:
            if not os.path.exists(new_directory):
                os.makedirs(data_directory)
                self.create_project_file(directory)
                return "New directory " + directory + " created"
            else:
                return "Directory already exists"
        except OSError:
            print('Error: Opening directory. ' + new_directory)

    # Create a default project.txt file
    def create_project_file(self, directory):
        project_file_dir = os.path.join(self.project_folder, directory, "project.txt")
        f = open(project_file_dir, "w+")
        f.write("name="+directory+"\n")
        f.write("dnn_type=cnn"+"\n")
        f.write("download_url="+"https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"+"\n")
        f.write("data_set_name="+"\n")
        f.write("epochs=10"+"\n")
        f.write("steps_per_epoch=0"+"\n")
        f.write("validation_steps=0"+"\n")
        f.write("loss_function=CategoricalCrossentropy"+"\n")
        f.write("optimizer=adam"+"\n")
        f.write("batch_size=64"+"\n")
        f.write("model_format=h5"+"\n")
        f.write("tf_lite_model=yes"+"\n")
        f.close()
        return "New project file for " + directory + " created"

    # Open specified project and return content of project.txt
    def open_project(self, directory):
        project_dir = os.path.join(self.project_folder, directory)
        project_file_dir = os.path.join(project_dir, "project.txt")
        try:
            if os.path.exists(project_dir):
                file = open(project_file_dir, "r")

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
        project_file_dir = os.path.join(self.project_folder, project.name[:-1], "project.txt")
        f = open(project_file_dir, "w+")
        f.write("name="+project.name +"\n")
        f.write("dnn_type="+project.dnn_type+"\n")
        f.write("download_url="+project.download_url+"\n")
        f.write("data_set_name="+project.data_set_name+ "\n")
        f.write("epochs="+project.epochs+"\n")
        f.write("steps_per_epoch="+project.steps_per_epoch+"\n")
        f.write("validation_steps="+project.validation_steps+"\n")
        f.write("loss_function="+project.loss_function+"\n")
        f.write("optimizer="+project.optimizer+"\n")
        f.write("batch_size="+project.batch_size+"\n")
        f.write("model_format="+project.model_format+"\n")
        f.write("tf_lite_model="+project.tf_lite_model+"\n")
        f.close()

    # Deleting a new folder for a project
    def delete_folder(self, directory):
        project_dir = os.path.join(self.project_folder, directory)
        try:
            if os.path.exists(project_dir):
                shutil.rmtree(project_dir)
                return "Project file deleted"
            else:
                return "Specified directory cannot be found"
        except OSError:
            print('Error: Deleting directory. ' + directory)
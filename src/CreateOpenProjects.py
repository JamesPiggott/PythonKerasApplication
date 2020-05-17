'''
Created on July 7 2018

@author: James Piggott

This class contains the functions to create and maintain projects
'''
import os
import glob
import shutil

from .project import Project

# List all files in /Projects folder - assuming they are projects
def list_all_projects():
    return os.listdir('../Projects/')

# Create a new folder for a project
def create_folder(directory):
    try:
        if not os.path.exists('../Projects/' + directory):
            os.makedirs('../Projects/' + directory + '/data')
            create_project_file(directory)
            return "New directory " + directory + " created"
        else:
            return "Directory already exists"
    except OSError:
        print('Error: Opening directory. ' + directory)

# Create a default project.txt file
def create_project_file(directory):
    f = open('../Projects/' + directory + "/project.txt", "w+")
    f.write("name="+directory+"\n")
    f.write("download_url="+"https://storage.googleapis.com/mledu-datasets/cats_and_dogs_filtered.zip"+"\n")
    f.write("epochs=10"+"\n")
    f.write("loss_function=CategoricalCrossentropy"+"\n")
    f.write("optimizer=adam"+"\n")
    f.write("batch_size=64"+"\n")
    f.write("model_format=h5"+"\n")
    f.close()

# Open specified project and return content of project.txt
def open_project(directory):
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


# Deleting a new folder for a project
def delete_folder(directory):
    try:
        if os.path.exists('../Projects/' + directory):
            shutil.rmtree('../Projects/' + directory)
            return "Project file deleted"
        else:
            return "Specified directory cannot be found"
    except OSError:
        print('Error: Deleting directory. ' + directory)

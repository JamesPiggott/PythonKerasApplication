'''
Created on July 7 2018

@author: James Piggott

This class contains the functions to create and maintain projects
'''
import os
import glob
import shutil

# List all files in /Projects folder - assuming they are projects
def list_all_projects():
    return os.listdir('../Projects/')

# Create a new folder for a project
def create_folder(directory):
    try:
        if not os.path.exists('../Projects/' + directory):
            os.makedirs('../Projects/' + directory + '/data')
            return "New directory " + directory + " created"
        else:
            return "Directory already exists"
    except OSError:
        print('Error: Opening directory. ' + directory)

# Open specified project and return content of project.txt
def open_project(directory):
    try:
        if os.path.exists('../Projects/' + directory):
            file = open('../Projects/' + directory + "/project.txt", "r")
            return "Project file opened", file
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

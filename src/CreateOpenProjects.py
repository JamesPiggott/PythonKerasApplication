'''
Created on July 7 2018

@author: James Piggott

This class contains the functions to create and maintain projects
'''
import os

def list_all_projects():
    print("The following project folder were detected")

# Create a new folder for a project
def create_folder(directory):
    try:
        if not os.path.exists('../Projects/' + directory):
            os.makedirs('../Projects/' + directory + '/data')
            return "New directory " + directory + " created"
        else:
            return "Directory already exists"
    except OSError:
        print('Error: Creating directory. ' + directory)

def open_project(directory):
    try:
        if os.path.exists('../Projects/' + directory):
            file = open('../Projects/' + directory + "project.txt", "r")
            print(file.read())
            return "Project file opened", file
        else:
            return "Project file could not be opened", None
    except OSError:
        print('Error: Creating directory. ' + directory)      


# Deleting a new folder for a project
def delete_folder(directory):
    try:
        if os.path.exists('../Projects/' + directory):
            shutil.rmtree('../Projects/' + directory)
        else:
            return "Specified directory cannot be found"
    except OSError:
        print('Error: Deleting directory. ' + directory)

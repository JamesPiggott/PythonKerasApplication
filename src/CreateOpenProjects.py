'''
Created on July 7 2018

@author: James Piggott

This class contains the functions to create and maintain projects
'''
import os, shutil


# Create a new folder for a project
def create_folder(directory):
    try:
        if not os.path.exists('../Projects/' + directory):
            os.makedirs('../Projects/' + directory)
            return "New directory " + directory + " created"
        else:
            return "Directory already exists"
    except OSError:
        print('Error: Creating directory. ' + directory)


# Deleting a new folder for a project
# def delete_folder(directory):
#     try:
#         if os.path.exists('../Projects/' + directory):
#             shutil.rmtree('../Projects/' + directory)
#         else:
#             return "Specified directory cannot be found"
#     except OSError:
#         print('Error: Deleting directory. ' + directory)


if __name__ == "__main__":
    folder_name = input()
    create_folder(folder_name)
    # delete_folder(folder_name)

'''
Created on May 21 2018

@author: James Piggott

This module reads in data for the application

Options include data on local hard-drive or from the internet.
Types of data includes images and CSV files that can be converted to data arrays in Numpy.

'''

import os


def askUserForOptions(project_name):

    # A project should already be selected
    project = '../Projects/' + project_name + '/data/'

    # Ask about local data or to download it from the internet
    data_set_completed = True
    while data_set_completed:

        # Check if data folder already contains data, if so ask to overwrite it
        if not os.listdir(project):
            print("Directory is empty. Please select data source option")
            print("1. Download data)")
            print("2. Copy-paste data")

            data_option = input()

            # If data source is from the internet, ask for URL
            if data_option is "1":
                download_data_set()

            # Else check if data folder contains files
            if data_option is "2":
                print()
            else:
                print("User selection is not valid.")

        else:
            print("Directory is not empty")


def download_data_set():
    print("Downloading data set")


if __name__ == "__main__":
    askUserForOptions()

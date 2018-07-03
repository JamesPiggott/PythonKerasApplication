'''
Created on May 21 2018

@author: James Piggott

This module reads in data for the application

Options include data on local hard-drive or from the internet.
Types of data includes images and CSV files that can be converted to data arrays in Numpy.

'''

from tkinter import *

import sys

def askUserForOptions():

    # A project should already be selected

    # Ask about local data or to download it from the internet

    # If data source is from the internet, ask for URL
    window = Tk()
    window.wm_title("Data URL ")
    User_input = Entry()
    User_input.pack()


    user_problem = (User_input.get())

    print(user_problem)

    window.mainloop()


if __name__ == "__main__":
    askUserForOptions()






'''
Created on April 7 2018

@author: James Piggott

Python application that can be used to cycle through workflow of a Deep Learning modelling task.
It uses Keras as a Deep Learning framework.
'''
import sys, src.CreateOpenProjects as projects


def exampleKerasApps():
    print("")
    print("Select application to run (you will be asked to confirm)")
    print("1. Neural Network (Boston Housing data)")
    print("2. Convolutional NN (MNIST-Fashion - Zalando")
    print("3. Recurrent NN (Stock market data)")
    print("4. Rest API (ImageNet)")
    print("5. Exoplanet CNN")
    print("0. Exit application")
    while(True):
        option = input()
        if option is "0":
            break
        if option is "1":
            run("Projects/Test_projects/KerasStart.py")
        if option is "2":
            run("Projects/Test_projects/KerasZalando.py")
        if option is "3":
            run("Projects/Test_projects/KerasStockPrediction.py")
        if option is "4":
            run("Projects/Test_projects/KerasRestApi.py")


def newKerasProject():
    print("1. Enter project name")
    print("2. Load data set")
    print("3. Analyze and pre-process data set")
    print("4. Define model")
    print("5. Train model using data set")
    print("6. Evaluate trained model")
    print("7. Perform steps 2 through 6 in sequence")
    print("0. Return to main menu")


    while True:
        project_option = input()

        if project_option is "0":
            break
        if project_option is "1":
            directory_name = input("Enter a name for your new Project: ")
            message = projects.create_folder(directory_name)
            print(message)
        # if project_option is "2":
        #     # analyzeDataSet()
        # if project_option is "3":
        #     # defineModel()
        # if project_option is "4":
        #     # trainModel()
        # if project_option is "5":
            # evaluateTrainedModel()
        if project_option is "6":
            break


def run(runfile):
    with open(runfile,"r") as rnf:
        exec(rnf.read())


def main():
    print("###################################################")
    print("####  Welcome to the Keras Deep learning tool   ###")
    print("###################################################")
    print(" ")

    while True:
        print(" ")
        print("Input an option below")
        print("1. Select example projects")
        print("2. Open or Create Keras project")
        print("0. Exit application")
        option = input()
        if option is "0":
            break
        if option is "1":
            exampleKerasApps()
        if option is "2":
            newKerasProject()
    sys.exit()


if __name__ == "__main__":
    main()
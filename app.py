'''
Created on April 7 2018

@author: James Piggott

Python application that can be used to cycle through workflow of a Deep Learning modelling task.
It uses Keras as a Deep Learning framework.
'''
import sys

from projects.test_projects.KerasStart import KerasStart
# from projects.test_projects.KerasRestApi import KerasRestApi
# from projects.test_projects.KerasRestApiSimpleRequest import KerasRestApiSimpleRequest
from projects.test_projects.KerasStockPrediction import KerasStockPrediction
from projects.test_projects.KerasZalando import KerasZalando
from projects.test_projects.KerasExoplanetCNN import KerasExoplanetCNN
from projects.test_projects.KerasAutoencoder import KerasAutoEncoder
from src.CreateOpenProjects import create_folder
from src.CreateOpenProjects import list_all_projects
from src.CreateOpenProjects import open_project
from src.CreateOpenProjects import delete_folder
from src.DefineModel import define_model
from src.DefineModel import set_optimizer
from src.DefineModel import set_data_augmentation
from src.AnalyzeDataSet import load_data
from src.AnalyzeDataSet import autodetect_data_format
from src.AnalyzeDataSet import transform_data
from src.TrainModel import train_model
from src.TrainModel import store_model
from src.EvaluateModel import evaluate_model

from tensorflow.python.client import device_lib

def get_available_gpus():
    local_device_protos = device_lib.list_local_devices()
    print("")
    print("Your system has the following devices available for Deep Learning")
    print("CPUs: ", [x.name for x in local_device_protos if x.device_type == 'CPU'])
    print("GPUs: ", [x.name for x in local_device_protos if x.device_type == 'GPU'])
    print("")

def ask_user_for_training_options(option):
    print("")
    print("Select training options: # epochs and model save choice")

    if option is "1":
        while True:
            print("For 'Boston Housing Data' 300 epochs are typical")
            epochs = int(input("Enter number of epochs: "))
            print("Do you wish to save the model to disk? [yes/Yes||no/No]")
            save_model = input("Enter choice: ")

            if epochs > 0 and epochs < 1000:
                if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                    return [epochs, True]
                else:
                    print("Please enter a choice that can be interpreted as 'yes' or 'no'")
            else:
                print("Please enter a sensible value between 0 and 1000")

    if option is "2":
        while True:
            print("For 'MNIST-Fashion Zalando' 20 epochs are typical")
            epochs = int(input("Enter number of epochs: "))
            print("Do you wish to save the model to disk? [yes/Yes||no/No]")
            save_model = input("Enter choice: ")

            if epochs > 0 and epochs < 100:
                if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                    return [epochs, True]
                else:
                    print("Please enter a choice that can be interpreted as 'yes' or 'no'")
            else:
                print("Please enter a sensible value between 0 and 100")

    if option is "3":
        print()

    if option is "4":
        print()

    if option is "5":
        while True:
            print("For 'Exoplanet CNN' 32 epochs are typical")
            epochs = int(input("Enter number of epochs: "))
            print("Do you wish to save the model to disk? [yes/Yes||no/No]")
            save_model = input("Enter choice: ")

            if epochs > 0 and epochs < 100:
                if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                    return [epochs, True]
                else:
                    print("Please enter a choice that can be interpreted as 'yes' or 'no'")
            else:
                print("Please enter a sensible value between 0 and 100")

    if option is "6":
        while True:
            print("For 'MNIST-AutoEncoder' 50 epochs are typical")
            epochs = int(input("Enter number of epochs: "))
            print("Do you wish to save the model to disk? [yes/Yes||no/No]: ")
            save_model = input("Enter choice: ")

            if epochs > 0 and epochs < 100:
                if save_model in ['y', 'Y', 'yes', 'Yes', 'YES', 'n', 'N', 'no', 'No', 'NO']:
                    return [epochs, True]
                else:
                    print("Please enter a choice that can be interpreted as 'yes' or 'no'")
            else:
                print("Please enter a sensible value between 0 and 100")

def example_keras_apps():

    run = True
    while run:

        print("")
        print("Select application to run (you will be asked to confirm)")
        print("1. Neural Network (Boston Housing data)")
        print("2. Convolutional NN (MNIST-Fashion - Zalando")
        print("3. Recurrent NN (Stock market data)")
        print("4. Rest API (ImageNet)")
        print("5. Exoplanet CNN")
        print("6. MNIST Autoencoder")
        print("0. Exit application")
        print("")

        option = input("Choose an option: ")
        if option is "0":
            break
        if option is "1":

            options = ask_user_for_training_options(option)
            confirmation = input("You will be training for " + str(options[0]) + " epochs. Are you certain? [yes/Yes||no/No]: ")

            if confirmation in ['yes', 'Yes']:
                keras_start = KerasStart()
                keras_start.start(options[0], options[1])

        if option is "2":

            options = ask_user_for_training_options(option)
            zalando = KerasZalando()
            zalando.start(options[0], options[1])

        if option is "3":

            stocks = KerasStockPrediction()
            stocks.start()

        if option is "4":
            run("Projects/Test_projects/KerasRestApi.py")

        if option is "5":

            options = ask_user_for_training_options(option)
            exoplanet = KerasExoplanetCNN()
            exoplanet.start(options[0], options[1])

        if option is "6":

            options = ask_user_for_training_options(option)
            autoencoder = KerasAutoEncoder()
            autoencoder.start(options[0], options[1])


def new_keras_project():

    while True:

        print("")
        print("1. Project management")
        print("2. Load data set")
        print("3. Define model")
        print("4. Train model using data set")
        print("5. Evaluate trained model")
        print("6. Perform steps 2 through 6 in sequence")
        print("7. Deployment")
        print("0. Return to main menu")
        print("")

        project_option = input("Choose an option: ")
        print("")

        if project_option is "0":
            break
        elif project_option is "1":
            project_management()
        elif project_option is "2":
            load_data()
            autodetect_data_format()
            transform_data()
        elif project_option is "3":
            define_model()
            set_optimizer()
            set_data_augmentation()
        elif project_option is "4":
            train_model()
            store_model()
        elif project_option is "5":
            evaluate_model()
        elif project_option is "6":
            print("TODO: cycle through the workflow automatically using project meta data")
        else:
            print("Not a valid option")

def project_management():

    while True:

        print("")
        print("1. List all projects")
        print("2. Open project file")
        print("3. Create new project")
        print("4. Delete project")
        print("0. Return to project overview menu")
        print("")

        project_option = input("Choose an option: ")
        print("")

        if project_option is "0": 
            break
        elif project_option is "1":

            print()
            print("The following project folder were detected")
            projects = list_all_projects()
            print()
            for project in projects:
                print(" # " + project)
            print()

        elif project_option is "2":

            directory_name = input("Enter the name of the project you want to open: ")
            message, file = open_project(directory_name)


        elif project_option is "3":

            directory_name = input("Enter a name for your new project: ")
            message, file = create_folder(directory_name)
            print(message)

        elif project_option is "4":

            directory_name = input("Enter name of project you want to delete: ")
            message = delete_folder(directory_name)
            print(message)

        else:
            print("Not a valid option")


def run(run_file):
    with open(run_file, "r") as rnf:
        exec(rnf.read())


def main():

    print(" ")
    print("###################################################")
    print("####  Welcome to the Keras Deep learning tool   ###")
    print("###################################################")
    print(" ")

    while True:

        print("")
        print("Input an option below")
        print("1. Select example projects")
        print("2. Open or Create Keras project")
        print("3. Detect hardware available")
        print("0. Exit application")
        print("")

        option = input("Choose an option: ")
        print("")

        if option is "0":
            break
        if option is "1":
            example_keras_apps()
        if option is "2":
            new_keras_project()
        if option is "3":
            get_available_gpus()
    sys.exit()


if __name__ == "__main__":
    main()

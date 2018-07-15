'''
Created on April 7 2018

@author: James Piggott

Python application that can be used to cycle through workflow of a Deep Learning modelling task.
It uses Keras as a Deep Learning framework.
'''
import sys
import src.CreateOpenProjects as projects
import src.AnalyzeDataSet as datasets
import src.DefineModel as model
import src.TrainModel as training
import src.EvaluateModel as evaluation


def example_keras_apps():
    print("")
    print("Select application to run (you will be asked to confirm)")
    print("1. Neural Network (Boston Housing data)")
    print("2. Convolutional NN (MNIST-Fashion - Zalando")
    print("3. Recurrent NN (Stock market data)")
    print("4. Rest API (ImageNet)")
    print("5. Exoplanet CNN")
    print("0. Exit application")
    while True:
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


def new_keras_project():
    print("1. Enter project name")
    print("2. Load data set")
    print("3. Define model")
    print("4. Train model using data set")
    print("5. Evaluate trained model")
    print("6. Perform steps 2 through 6 in sequence")
    print("0. Return to main menu")

    while True:
        project_option = input()

        if project_option is "0":
            break
        elif project_option is "1":
            directory_name = input("Enter a name for your new Project: ")
            message = projects.create_folder(directory_name)
            print(message)
        elif project_option is "2":
            datasets.load_data()
            datasets.autodetect_data_format()
            datasets.transform_data()
        elif project_option is "3":
            model.define_model()
            model.set_optimizer()
            model.set_data_augmentation()
        elif project_option is "4":
            training.train_model()
            training.store_model()
        elif project_option is "5":
            evaluation.evaluate_model()
        elif project_option is "6":
            print("TODO: cycle through the workflow automatically using project meta data")
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
        print(" ")
        print("Input an option below")
        print("1. Select example projects")
        print("2. Open or Create Keras project")
        print("0. Exit application")
        option = input()
        if option is "0":
            break
        if option is "1":
            example_keras_apps()
        if option is "2":
            new_keras_project()
    sys.exit()


if __name__ == "__main__":
    main()

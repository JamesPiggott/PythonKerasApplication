'''
Created on April 7 2018

@author: James Piggott

Keras example using the Fashion-MNIST images from Zalando
'''
import sys
from subprocess import Popen

def exampleKerasApps():
    print("")
    print("Select application to run (you will be asked to confirm)")
    print("1. Neural Network (Boston Housing data)")
    print("2. Convolutional NN (MNIST-Fashion - Zalando")
    print("3. Recurrent NN (Stock market data")
    print("4. Rest API (ImageNet)")
    print("0. Exit application")
    while(True):
        option = input()
        if option is "0":
            break
        if option is "1":
            run("KerasStart.py")
        if option is "2":
            run("KerasZalando.py")
        if option is "3":
            run("src/KerasStockPrediction.py")
        if option is "4":
            run("KerasRestApi.py")

def newKerasProject():
    print("")

def run(runfile):
  with open(runfile,"r") as rnf:
    exec(rnf.read())

def main():
    print("###################################################")
    print("####  Welcome to the Keras Deep learning tool   ###")
    print("###################################################")
    print(" ")
    while(True):
        print(" ")
        print("Input an option below")
        print("1. Select example projects")
        print("2. Create new Keras project")
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
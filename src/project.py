from data import Data


class Project:

    name = ""
    epochs = ""
    loss_function = ""
    optimizer = ""
    batch_size = ""
    model_format = ""

    data = Data

    """Represent the high-level definition of a Project"""
    def __init__(self):
        self.name = ""
        self.epochs = ""
        self.loss_function = ""
        self.optimizer = ""
        self.batch_size = ""
        self.model_format = ""

    def parse_input(self, file):
        print("")
        for key in file.keys():
            if key == "name":
                self.name = key
                print(key + " " + file[key])
            elif key == "epochs":
                self.epochs = key
                print(key + " " + file[key])
            elif key == "loss_function":
                self.loss_function = key
                print(key + " " + file[key])
            elif key == "optimizer":
                self.optimizer = key
                print(key + " " + file[key])
            elif key == "batch_size":
                self.batch_size = key
                print(key + " " + file[key])
            elif key == "model_format":
                self.model_format = key
                print(key + " " + file[key])
            else:
                print(key + " is an undefined keyword")

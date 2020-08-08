from .data import Data


class Project:

    """Represent the high-level definition of a Project"""
    def __init__(self):
        self.name = ""
        self.dnn_type = ""
        self.download_url = ""
        self.data_set_name = ""
        self.epochs = ""
        self.steps_per_epoch = ""
        self.validation_steps = ""
        self.loss_function = ""
        self.optimizer = ""
        self.batch_size = ""
        self.model_format = ""
        self.tf_lite_model = ""
        self.data = Data()

    def parse_input(self, file):
        print("")
        for key in file.keys():
            if key == "name":
                self.name = file[key]
                print(key + " " + file[key])
            elif key == "dnn_type":
                self.dnn_type = file[key]
                print(key + " " + file[key])
            elif key == "download_url":
                self.download_url = file[key]
                print(key + " " + file[key])
            elif key == "data_set_name":
                self.data_set_name = file[key]
                print(key + " " + file[key])
            elif key == "epochs":
                self.epochs = file[key]
                print(key + " " + file[key])
            elif key == "steps_per_epoch":
                self.steps_per_epoch = file[key]
                print(key + " " + file[key])
            elif key == "validation_steps":
                self.validation_steps = file[key]
                print(key + " " + file[key])
            elif key == "loss_function":
                self.loss_function = file[key]
                print(key + " " + file[key])
            elif key == "optimizer":
                self.optimizer = file[key]
                print(key + " " + file[key])
            elif key == "batch_size":
                self.batch_size = file[key]
                print(key + " " + file[key])
            elif key == "model_format":
                self.model_format = file[key]
                print(key + " " + file[key])
            elif key == "tf_lite_model":
                self.tf_lite_model = file[key]
                print(key + " " + file[key])
            else:
                print(key + "an undefined keyword")

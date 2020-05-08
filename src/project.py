class Project:

    name = ""
    epochs = ""
    loss_function = ""
    optimizer = ""
    batch_size = ""
    model_format = ""

    """Represent the high-level definition of a Project"""
    def __init__(self):
        self.name = ""
        self.epochs = ""
        self.loss_function = ""
        self.optimizer = ""
        self.batch_size = ""
        self.model_format = ""

    def parse_input(self, file):
        for key in file.keys():
            print(key + " " + file[key])

            if key is "name":
                self.name = key
                print(key + " " + file[key])
            if key is "epochs":
                self.epochs = key
                print(key + " " + file[key])
            if key is "loss_function":
                self.loss_function = key
                print(key + " " + file[key])
            if key is "optimizer":
                self.optimizer = key
                print(key + " " + file[key])
            if key is "batch_size":
                self.batch_size = key
                print(key + " " + file[key])
            if key is "model_format":
                self.model_format = key
                print(key + " " + file[key])
            else:
                print("Undefined keyword")

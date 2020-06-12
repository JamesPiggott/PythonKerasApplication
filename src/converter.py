import tensorflow as tf


class Converter:

    model_format = ""

    """Contains functions to convert models to other formats: h5, JSON and TF lite"""
    def __init__(self):
        self.model_format = ""


    def from_keras_to_json(self):
        # saved_model_path = "./{}.h5".format(int(time.time()))

        # model.save(saved_model_path)

        # command line argument
        # !tensorflowjs_converter --input_format=keras {saved_model_path} ./

        print("from_keras_to_json")


    def from_saved_model_to_tflite(self):
        print("from_saved_model_to_tflite")


    def from_keras_to_tflite(self):
        print("from_keras_to_tflite")


    def from_concrete_functions_to_tflite(self):
        print("from_concrete_functions_to_tflite")

    def optimization_of_model(self):
        mode = "Speed" 

        if mode == 'Storage':
            optimization = tf.lite.Optimize.OPTIMIZE_FOR_SIZE
        elif mode == 'Speed':
            optimization = tf.lite.Optimize.OPTIMIZE_FOR_LATENCY
        else:
            optimization = tf.lite.Optimize.DEFAULT






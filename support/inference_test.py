import tensorflow as tf
import PIL
import PIL.Image
from matplotlib import pyplot as plt
import numpy as np

from keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array



class Test:

    def __init__(self):


        # self.load_data()
        # self.convert_data()
        # self.define_model(1, 64)
        # self.set_optimizer()
        # self.train_model()
        # self.evaluate_model()
        # self.store_model("")
        self.load_model("")
        self.perform_inference()

    def store_model(self, path):
        print("Store the model")
        saved_model_path = 'test_model.h5'
        self.model.save(path + saved_model_path)
        del self.model

    def load_model(self, path):
        print("Load the model")
        saved_model_path = 'test_model.h5'
        self.model = tf.keras.models.load_model(path + saved_model_path)

    def load_image(self, filename):
        print("Load an image")
        img = load_img(filename, grayscale=True, target_size=(28, 28))
        img = img_to_array(img)
        img = img.reshape(1, 28, 28, 1)
        img = img.astype('float32')
        img = img / 255.0
        return img

    def perform_inference(self):
        img = self.load_image('test.png')
        result = self.model.predict_classes(img)
        print(result[0])
import requests 
import zipfile
import os
class Data:
    data_set_name = ""
    train_dir = ""
    validation_dir = ""
    train_cats_dir = ""
    train_dogs_dir = ""
    validation_cats_dir = ""
    validation_dogs_dir = ""
    train_cat_fnames = ""
    train_dog_fnames = ""

    '''
    Created on July 15 2018

    @author: James Piggott

    This class contains the functions to that will analyze and transform the data set for use with Keras.
    '''
    """Represent the high-level definition of a Project"""
    def __init__(self):
        print("Init")

        self.data_set_name = ""
        self.train_dir = ""
        self.validation_dir = ""
        self.validation_cats_dir = ""
        self.validation_dogs_dir = ""
        self.train_cat_fnames = ""
        self.train_dog_fnames = ""


    def download_url(self, url, save_path, chunk_size=128):
        print("URL: " + url)
        r = requests.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def unzip_data_file(self, save_path):
        local_zip = save_path
        zip_ref = zipfile.ZipFile(local_zip, 'r')
        data_name = zip_ref.namelist()[0][:-1]
        self.data_set_name = data_name
        zip_ref.extractall(save_path + "../../")
        zip_ref.close()


    def load_data_cnn(self, data_location):
        print("Load datas")


    def load_data(self, data_location):

        base_dir = os.path.join(data_location, self.data_set_name)
        self.train_dir = os.path.join(base_dir, 'train')
        self.validation_dir = os.path.join(base_dir, 'validation')

        data_categories = os.listdir(self.train_dir)

        train_set = []
        for cat in data_categories:
            train_set.append(os.path.join(self.train_dir, cat))

        val_set = []
        for cat in data_categories:
            val_set.append(os.path.join(self.validation_dir, cat))

        for training in train_set:
            print('total training '+ cat +' images :', len(os.listdir(training)))

        for validation in val_set:
            print('total validation '+ cat +' images :', len(os.listdir(validation)))

        # sample_files = []
        # for train in train_set:
        #     sample_files.append(os.listdir(train))


    def autodetect_data_format(self):
        print("Checking what format data files have")


    def transform_data(self):
        print("Transforming data set into suitable format")

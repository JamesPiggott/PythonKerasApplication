import requests 
import zipfile
import os
class Data:

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
        # global validation_cats_dir
        # global validation_dogs_dir
        # global train_cat_fnames
        # global train_dog_fnames
        # train_cats_dir = ""
        # train_dogs_dir = ""
        validation_cats_dir = ""
        validation_dogs_dir = ""
        train_cat_fnames = ""
        train_dog_fnames = ""


    def download_url(self, url, save_path, chunk_size=128):
        r = requests.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def unzip_data_file(self, save_path):
        local_zip = save_path
        zip_ref = zipfile.ZipFile(local_zip, 'r')
        zip_ref.extractall(save_path + "../../")
        zip_ref.close()

    def load_data(self, data_location):
        base_dir = data_location + '/cats_and_dogs_filtered'

        train_dir = os.path.join(base_dir, 'train')
        validation_dir = os.path.join(base_dir, 'validation')

        # Directory with our training cat/dog pictures
        train_cats_dir = os.path.join(train_dir, 'cats')
        train_dogs_dir = os.path.join(train_dir, 'dogs')
        print(train_cats_dir)

        # Directory with our validation cat/dog pictures
        validation_cats_dir = os.path.join(validation_dir, 'cats')
        validation_dogs_dir = os.path.join(validation_dir, 'dogs')

        print(validation_cats_dir)

        # List categories
        self.train_cat_fnames = os.listdir( train_cats_dir )
        self.train_dog_fnames = os.listdir( train_dogs_dir )

        print(self.train_cat_fnames[:10])
        print(self.train_dog_fnames[:10])

        print('total training cat images :', len(os.listdir(      train_cats_dir ) ))
        print('total training dog images :', len(os.listdir(      train_dogs_dir ) ))

        print('total validation cat images :', len(os.listdir( self.validation_cats_dir ) ))
        print('total validation dog images :', len(os.listdir( self.validation_dogs_dir ) ))

        print("Loading data for project: ")


    def autodetect_data_format(self):
        print("Checking what format data files have")


    def transform_data(self):
        print("Transforming data set into suitable format")

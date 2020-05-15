import requests 

class Data:


    '''
    Created on July 15 2018

    @author: James Piggott

    This class contains the functions to that will analyze and transform the data set for use with Keras.
    '''

    def download_url(self, url, save_path, chunk_size=128):
        r = requests.get(url, stream=True)
        with open(save_path, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=chunk_size):
                fd.write(chunk)

    def load_data(self):
        print("Loading data for project: ")


    def autodetect_data_format(self):
        print("Checking what format data files have")


    def transform_data(self):
        print("Transforming data set into suitable format")

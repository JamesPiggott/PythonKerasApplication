import kivy
from kivy.app import App
from kivy.lang import Builder
import kivy_garden.contextmenu

from tensorflow.python.client import device_lib

class MenuApp(App):
    def build(self):
        self.title = 'Simple app menu example'
        return Builder.load_file('kv/menu.kv')

    def get_available_gpus(self):
        local_device_protos = device_lib.list_local_devices()
        print("")
        print("Your system has the following devices available for Deep Learning")
        print("CPUs: ", [x.name for x in local_device_protos if x.device_type == 'CPU'])
        print("GPUs: ", [x.name for x in local_device_protos if x.device_type == 'GPU'])
        print("")

if __name__ == '__main__':
    MenuApp().run()
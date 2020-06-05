import subprocess

from tensorflow.python.client import device_lib

class System:

    def __init__(self):
        print()

    def get_available_gpus(self):
        local_device_protos = device_lib.list_local_devices()
        print("")
        print("Your system has the following devices available for Deep Learning")
        print("CPUs: ", [x.name for x in local_device_protos if x.device_type == 'CPU'])
        print("GPUs: ", [x.name for x in local_device_protos if x.device_type == 'GPU'])
        print("")

    def check_docker_availability(self):
        print("")
        print("Your system has the following Docker version installed")
        subprocess.call("docker -v", shell=True)
        print("")

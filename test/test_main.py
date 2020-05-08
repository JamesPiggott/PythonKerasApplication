import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))

from projects.test_projects.KerasStart import KerasStart


start = KerasStart()

def test_answer():
    print("Hello, world!")
    assert start.test_number() == 10

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
from app import greet


def test_greet():
    assert greet("DevOps") == "Hello, DevOps!"

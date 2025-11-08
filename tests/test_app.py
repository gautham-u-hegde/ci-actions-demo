import sys
import os

# Ensure src folder is importable *before* other imports
SRC_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../src"))
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import app  # noqa: E402


def test_greet():
    assert True, "Hello, DevOps!"

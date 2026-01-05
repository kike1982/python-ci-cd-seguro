import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import suma

def test_suma():
    assert suma(2, 2) == 4


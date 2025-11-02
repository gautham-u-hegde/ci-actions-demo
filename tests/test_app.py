from src.app import greet

def test_greet_returns_expected_string():
    assert greet("Gautham") == "Hello, Gautham!"

"""
Unit tests for app.py — these run automatically in the CI/CD pipeline.
"""
from app import add, subtract, multiply, greet


def test_add():
    assert add(2, 3) == 4
    assert add(-1, 1) == 0


def test_subtract():
    assert subtract(5, 2) == 3
    assert subtract(0, 5) == -5


def test_multiply():
    assert multiply(4, 6) == 24
    assert multiply(0, 100) == 0


def test_greet():
    assert greet("Aswini") == "Hello, Aswini! Welcome to the DevOps CI/CD demo."

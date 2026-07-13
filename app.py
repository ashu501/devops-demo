"""
Simple demo application for CI/CD Pipeline demonstration.
DevOps Lab - ACE Engineering College
"""


def add(a, b):
    """Add two numbers."""
    return a + b


def subtract(a, b):
    """Subtract b from a."""
    return a - b


def multiply(a, b):
    """Multiply two numbers."""
    return a * b


def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the DevOps CI/CD demo."


if __name__ == "__main__":
    print(greet("ACE Students"))
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("4 * 6 =", multiply(4, 6))

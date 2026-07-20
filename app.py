"""
Simple demo application for CI/CD Pipeline demonstration.

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


def divide(a, b):
    """Divide a by b."""
    if b == 0:
        return "Cannot divide by zero"
    return a / b


def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}! Welcome to the DevOps CI/CD demo."


def run_demo():
    """Returns the demo output as a list of strings - this makes it testable."""
    lines = []
    lines.append(greet("ACE Students"))
    lines.append(f"2 + 3 = {add(2, 3)}")
    lines.append(f"5 - 2 = {subtract(5, 2)}")
    lines.append(f"4 * 6 = {multiply(4, 6)}")
    lines.append(f"10 / 2 = {divide(10, 2)}")
    return lines


if __name__ == "__main__":
    for line in run_demo():
        print(line)
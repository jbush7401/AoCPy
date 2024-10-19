import os

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

def read_input_file(filename):
    filename = os.path.join(PROJECT_ROOT, filename)
    with open(filename, 'r') as file:
        return [line.strip() for line in file]
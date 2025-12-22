import os


def my_write(path, data):
    with open(os.path.join(os.path.dirname(__file__), '../../../docs/', path), 'w') as f:
        f.write(data)
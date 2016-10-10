"""
The bridge pattern is a design pattern used in software engineering which is meant to "decouple an abstraction from its
implementation so that the two can vary independently". The bridge uses encapsulation, aggregation, and can use
inheritance to separate responsibilities into different classes.
"""
import os


class FilePath(object):
    def create_file_path_1(self, dir_path, file_name):
        return os.path.join(dir_path, file_name)


class Bridge(object):
    def __init__(self):
        self.implem = FilePath()

    def create_file_path_2(self, dir_path, file_name, extenstion):
        return self.implem.create_file_path_1(dir_path, file_name + "." + extenstion)


if __name__ == '__main__':
    print(FilePath().create_file_path_1('/tmp/', 'filename'))
    print(Bridge().create_file_path_2('/tmp/', 'filename', 'jpg'))

"""
Decouple an abstraction from its implementation so that the two can vary independently.
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


print(FilePath().create_file_path_1('/tmp/', 'filename'))

print(Bridge().create_file_path_2('/tmp/', 'filename', 'jpg'))

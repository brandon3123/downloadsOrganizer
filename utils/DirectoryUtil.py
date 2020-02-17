import os
import shutil

from os import path
from enums.Extension import Extension

FORWARD_SLASH = '/'


class DirectoryUtil:

    @staticmethod
    def create_directory_at_path(path, directory_name):
        os.mkdir(path + FORWARD_SLASH + directory_name)

    @staticmethod
    def move_file_to_directory(directory, file):
        shutil.move(file, directory)

    @staticmethod
    def get_file_extension(event):
        extension = path.splitext(event)[1][1::]
        try:
            return Extension[extension.upper()]
        except:
            return Extension.UNKNOWN

    @staticmethod
    def get_file_path(event):
        return event.rsplit(FORWARD_SLASH, 1)[0]

    @staticmethod
    def get_file_name(event):
        file_name = path.basename(event).rsplit('.')[0]
        return file_name

    @staticmethod
    def does_directory_exist_in_path(working_directory, directory_name):
        return path.exists(working_directory + FORWARD_SLASH + directory_name)

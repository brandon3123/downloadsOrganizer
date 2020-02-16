import os
import shutil
import datetime

from os import path
from enums.Extension import Extension


def does_directory_exist_in_path(working_directory, directory_name):
    return path.exists(working_directory + '/' + directory_name)


class DirectoryUtil:

    @staticmethod
    def does_current_date_directory_exist_in_path(working_directory):
        return does_directory_exist_in_path(working_directory, str(datetime.date.today()))

    @staticmethod
    def create_directory_at_path(path, directory_name):
        os.mkdir(path + '/' + directory_name)

    @staticmethod
    def move_file_to_directory(directory, file):
        shutil.move(file, directory)

    @staticmethod
    def get_file_extension(event):
        extension = path.splitext(event)[1][1::]
        return Extension[extension.upper()]

    @staticmethod
    def get_file_path(event):
        return event.rsplit('/', 1)[0]

    @staticmethod
    def get_file_name(event):
        file_name = path.basename(event).rsplit('.')[0]
        return file_name

    @staticmethod
    def does_directory_exist_for_extension_at_path(path, extension):
        return does_directory_exist_in_path(path, extension.value)
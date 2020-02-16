import os
import shutil
import datetime

from os import path
from enums.Extension import Extension

DOWNLOADS = '/Users/brandon/Downloads/organizer'


def does_directory_exist_in_working_directory(working_directory, directory_name):
    return path.exists(working_directory + '/' + directory_name)


class DirectoryUtil:

    @staticmethod
    def current_date_directory_exist_in_working_directory(working_directory):
        return path.exists(working_directory + '/' + datetime.date.today())

    @staticmethod
    def create_directory(directory_name):
        os.mkdir(DOWNLOADS + '/' + directory_name)

    @staticmethod
    def move_file_to_directory(directory, file):
        shutil.move(directory, file)

    @staticmethod
    def get_file_extension(file):
        return Extension[file[-3:].upper()]

    @staticmethod
    def does_directory_exist_for_extension(extension):
        return does_directory_exist_in_working_directory(DOWNLOADS, extension.value)
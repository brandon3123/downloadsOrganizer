import datetime

from watchdog.events import FileSystemEventHandler
from utils.DirectoryUtil import DirectoryUtil
from model.FileMetaData import FileMetaData


class DirectoryEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        super(DirectoryEventHandler, self).on_created(event)
        perform_cleanup_for_directory(event)


def perform_cleanup_for_directory(event):
    if not event.is_directory:

        file = FileMetaData(event)

        if DirectoryUtil.does_directory_exist_for_extension_at_path(file.path, file.extension):
            perform_cleanup_existing_extension_directory(file)
        else:
            perform_cleanup_absent_extension_directory(file)


def perform_cleanup_existing_extension_directory(file):
    extension_directory = file.path + '/' + file.extension.value

    today = today_date_string()

    today_directory = extension_directory + '/' + today

    if not DirectoryUtil.does_current_date_directory_exist_in_path(extension_directory):
        DirectoryUtil.create_directory_at_path(extension_directory, today)

    DirectoryUtil.move_file_to_directory(today_directory, file.full_file_path)


def perform_cleanup_absent_extension_directory(file):
    DirectoryUtil.create_directory_at_path(file.path, file.extension.value)
    perform_cleanup_existing_extension_directory(file)


def today_date_string():
    return str(datetime.date.today())

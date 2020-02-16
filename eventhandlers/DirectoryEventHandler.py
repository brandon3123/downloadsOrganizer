import datetime

from watchdog.events import FileSystemEventHandler
from utils.DirectoryUtil import DirectoryUtil
from model.FileMetaData import FileMetaData

TODAY = str(datetime.date.today())


class DirectoryEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        super(DirectoryEventHandler, self).on_created(event)

        if not event.is_directory:
            file_extension = DirectoryUtil.get_file_extension(event.src_path)
            file_path = DirectoryUtil.get_file_path(event.src_path)
            file_name = DirectoryUtil.get_file_name(event.src_path)

            file = FileMetaData(file_name, file_extension, file_path)

            perform_cleanup_for_directory(file, event)


def perform_cleanup_for_directory(file, event):
    if DirectoryUtil.does_directory_exist_for_extension_at_path(file.path, file.extension):
        perform_cleanup_existing_extension_directory(file, event)
    else:
        perform_cleanup_absent_extension_directory(file, event)


def perform_cleanup_existing_extension_directory(file, event):
    extension_directory = file.path + '/' + file.extension.value

    today_directory = extension_directory + '/' + TODAY

    if not DirectoryUtil.does_current_date_directory_exist_in_path(extension_directory):
        DirectoryUtil.create_directory_at_path(extension_directory, TODAY)

    DirectoryUtil.move_file_to_directory(today_directory, event.src_path)


def perform_cleanup_absent_extension_directory(file, event):
    DirectoryUtil.create_directory_at_path(file.path, file.extension.value)
    perform_cleanup_existing_extension_directory(file, event)

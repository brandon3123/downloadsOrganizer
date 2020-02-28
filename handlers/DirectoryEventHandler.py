import datetime
import time

from watchdog.events import FileSystemEventHandler
from utils.DirectoryUtil import DirectoryUtil
from model.FileMetaData import FileMetaData
from enums.Constant import Constant


class DirectoryEventHandler(FileSystemEventHandler):
    """
    Class to handle events from our observer inside directoryOrganizer.py.
    Once an event is fired, we listen for "on_created" events which will then
    be organized into the following folder structure.

        -Type (pdf)
            - Date
                -File
        -Type (csv)
            - Date
                -File
    """

    def on_created(self, event):
        time.sleep(5)
        super(DirectoryEventHandler, self).on_created(event)
        perform_cleanup_for_directory(event)


def perform_cleanup_for_directory(event):
    if not event.is_directory and not event.src_path.endswith('DS_Store') and not '.com.google' in event.src_path:

        file = FileMetaData(event)

        if DirectoryUtil.does_directory_exist_in_path(file.path, file.extension.value):
            perform_cleanup_existing_extension_directory(file)
        else:
            perform_cleanup_absent_extension_directory(file)


def perform_cleanup_existing_extension_directory(file):
    today = today_date_string()

    if not DirectoryUtil.does_directory_exist_in_path(file.extension_directory(), today):
        DirectoryUtil.create_directory_at_path(file.extension_directory(), today)

    today_directory = file.extension_directory() + Constant.FORWARD_SLASH.value + today
    DirectoryUtil.move_file_to_directory(today_directory, file.full_file_path)


def perform_cleanup_absent_extension_directory(file):
    DirectoryUtil.create_directory_at_path(file.path, file.extension.value)
    perform_cleanup_existing_extension_directory(file)


def today_date_string():
    """ Returns a string representation of the current date. """
    return str(datetime.date.today())

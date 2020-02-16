from watchdog.events import FileSystemEventHandler
from utils.DirectoryUtil import DirectoryUtil

DOWNLOADS = '/Users/brandon/Downloads'


def perform_cleanup_for_extension(extension):
    if DirectoryUtil.does_directory_exist_for_extension(extension):
        print('yes')
    else:
        DirectoryUtil.create_directory(extension.value)


class DirectoryEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        super(DirectoryEventHandler, self).on_created(event)

        if event.is_directory:
            print()  # ignore
        else:
            extension = DirectoryUtil.get_file_extension(event.src_path)
            perform_cleanup_for_extension(extension)




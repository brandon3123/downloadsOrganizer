from utils.DirectoryUtil import DirectoryUtil
from enums.Constant import Constant


class FileMetaData:

    def __init__(self, event):
        self.path = DirectoryUtil.get_file_path(event.src_path)
        self.name = DirectoryUtil.get_file_name(event.src_path)
        self.extension = DirectoryUtil.get_file_extension(event.src_path)
        self.full_file_path = event.src_path

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def extension(self):
        return self._extension

    @extension.setter
    def extension(self, extension):
        self._extension = extension

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def full_file_path(self):
        return self._full_file_path

    @full_file_path.setter
    def full_file_path(self, full_file_path):
        self._full_file_path = full_file_path

    def extension_directory(self):
        return self._path + Constant.FORWARD_SLASH.value + self._extension.value

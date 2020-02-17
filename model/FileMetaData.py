class FileMetaData:

    def __init__(self, name, extension, path):
        self.path = path
        self.name = name
        self.extension = extension

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

    def full_file_path(self):
        return self._path + '/' + self._name + '.' + self._extension

    def name_with_extension(self):
        return self._name + '.' + self._extension

    def name_with_path(self):
        return self._path + '/' + self._name

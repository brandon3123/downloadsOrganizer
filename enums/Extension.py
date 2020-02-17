from aenum import Enum, NoAlias


class Extension(Enum, settings=NoAlias):
    PDF = 'pdf'
    TXT = 'text'
    DOCX = 'word'
    PNG = 'images'
    JPG = 'images'
    ZIP = 'zipped'
    GZ = 'zipped'
    CSV = 'csv-excel'
    XLSX = 'csv-excel'
    JSON = 'json'
    EXE = 'applications'
    APP = 'applications'
    DMG = 'applications'
    PKG = 'applications'
    ISO = 'iso-image'
    JAVA = 'java-app'
    CLASS = 'java-class'
    PYC = 'python-app'
    UNKNOWN = 'misc'

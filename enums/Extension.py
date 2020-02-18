from aenum import Enum, NoAlias


class Extension(Enum, settings=NoAlias):
    """
        File extensions handled and there associated folder names.
    """
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
    OVA = 'os-image'
    JAVA = 'java-app'
    CLASS = 'java-class'
    PYC = 'python-app'
    XML = 'xml'
    SVG = 'vectors'
    CERT = 'certificates'
    UNKNOWN = 'misc'

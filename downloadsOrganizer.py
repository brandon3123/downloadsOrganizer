from watchdog.observers import Observer
from handlers.DirectoryEventHandler import DirectoryEventHandler

DIRECTORY_TO_WATCH = '/Users/brandon/Downloads/organizer'

if __name__ == "__main__":

    event_handler = DirectoryEventHandler()
    observer = Observer()
    observer.schedule(event_handler, DIRECTORY_TO_WATCH, recursive=True)
    observer.start()

    try:
        while observer.is_alive():
            observer.join(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

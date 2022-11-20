import logging
import time
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


class MyEventHandler(FileSystemEventHandler):
    def catch_all_handler(self, event):
        logging.debug(event)
        print("1")
        print(event)

    def on_moved(self, event):
        self.catch_all_handler(event)
        print("2")
        print(event)

    def on_created(self, event):
        self.catch_all_handler(event)
        print("3")
        print(event)

    def on_deleted(self, event):
        self.catch_all_handler(event)
        print("4")
        print(event)

    def on_modified(self, event):
        self.catch_all_handler(event)
        print("5")
        print(event)

path = '/Users/konstantinirosnikov/Desktop/testPy'

event_handler = MyEventHandler()
observer = Observer()
observer.schedule(event_handler, path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()
observer.join()

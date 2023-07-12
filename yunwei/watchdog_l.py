from watchdog.observers import Observer
from watchdog.events import *
import time


class FileEventHandle(FileSystemEventHandler):
    def __init__(self):
        FileSystemEventHandler.__init__(self)
    def on_moved(self, event):
         now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
         if event.is_directory:
             print(f"{ now } dir {event.src_path} moved to {event.dest_path}" )
         else:
             print(f"{now} file {event.src_path} moved to {event.dest_path}")
    def on_created(self, event):
         now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
         if event.is_directory:
             print(f"{ now } dir {event.src_path} created" )
         else:
             print(f"{now} file {event.src_path} created")
    def on_deleted(self, event):
         now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
         if event.is_directory:
             print(f"{ now } dir {event.src_path} delete " )
         else:
             print(f"{now} file {event.src_path} delete ")

    def on_modified(self, event):
         now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
         if event.is_directory:
             print(f"{ now } dir {event.src_path} modify " )
         else:
             print(f"{now} file {event.src_path} modify ")


if __name__ == "__main__":
    observer = Observer()
    path = r"/home/yangrudan/Desktop/"
    evnet_handle = FileEventHandle()
    observer.schedule(evnet_handle, path, True)  #True diguizimulu
    print(f"Monitor {path}")
    observer.start()
    observer.join()
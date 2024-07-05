#!/usr/bin/env python3
import threading
import time
import os

class FileWatcher():
    def __init__(self, filename, callback):
        self.filename = filename
        self.callback = callback
        self.thread = None
        self.__thread_going = False
    def start(self):
        self.__thread_going = True
        self.thread = threading.Thread(target=self.__thread_function, args=(), daemon=True)
        self.thread.start()
    def stop(self):
        self.__thread_going = False
        self.join()
    def join(self):
        self.thread.join()
    def __thread_function(self):
        original_time = os.path.getmtime(self.filename)
        while(self.__thread_going):
            mod_time = os.path.getmtime(self.filename)
            if (mod_time > original_time):
                # Call callback
                self.callback()
                # Prevent read until it's changed again
                original_time = mod_time
            time.sleep(0.1)


def test_callback():
    print(f"in callback")

if __name__ == "__main__":
    fw = FileWatcher("events.json", test_callback)
    fw.start()
    time.sleep(2)
    fw.stop()


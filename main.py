#!/usr/bin/env python3
import time
from watcher import FileWatcher
from read import FileRead
from state import Events
from state import States

def trigger_event(state, event):
    new_state = state
    if event == Events.READY_TO_WAIT:
        new_state = States.WAIT
    elif event == Events.STARTING:
        new_state = States.IN_PROGRESS
    elif event == Events.COMPLETE:
        new_state = States.DONE
    return new_state

class Main():
    def __init__(self):
        self.filename = "events.json"
        self.filewatcher = FileWatcher(self.filename, self.__file_change_callback)
        self.state = States.IDLE
        self.reader = FileRead(self.filename)
    def loop(self):
        self.filewatcher.start()
        # Wait until done.
        while self.state != States.DONE:
            time.sleep(0.1)
        self.filewatcher.stop()
    def __write_state(self):
        with open("state.txt", "w") as state_file:
            state_file.write(str(self.state.name))
    def __file_change_callback(self):
        # read file
        event_string = self.reader.get_event_string()
        event = Events[event_string]
        self.state = trigger_event(self.state, event)
        self.__write_state()

main = Main()
main.loop()


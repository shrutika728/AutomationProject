#!/usr/bin/env python3
import json

class FileRead():
    def __init__(self, filename):
        self.filename = filename
    def get_event_string(self):
        with open(self.filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data['event']

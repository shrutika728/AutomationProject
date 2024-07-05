#!/usr/bin/env python3
from enum import Enum, unique, auto
from re import sub

@unique
class Events(Enum):
    READY_TO_WAIT = auto()
    STARTING = auto()
    COMPLETE = auto()

@unique
class States(Enum):
    IDLE = auto()
    WAIT = auto()
    IN_PROGRESS = auto()
    DONE = auto()


# road.py
from enum import Enum

class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class Road:
    def __init__(self, name, locX=None, locY=None, len=None, hdg=None):
        self.name = name
        self.length = len
        self.heading = hdg
        self.xlocation = locX
        self.ylocation = locY

    def get_length(self):
        return self.length

    def get_xlocation(self):
        return self.xlocation

    def get_ylocation(self):
        return self.ylocation

    def get_heading(self):
        return self.heading

    def get_road_name(self):
        return self.name
    
    def print(self, print_driver, obj):
        print_driver.print_road(self, obj)

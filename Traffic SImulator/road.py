from abc import ABC
from enum import Enum

class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class Road:
    NumOfRoads = 0

    def __init__(self, street_name, loc_x, loc_y, length, hdg):
        self.road_items = []
        self.name = street_name
        self.length = length
        self.heading = hdg
        self.xlocation = loc_x
        self.ylocation = loc_y
        Road.NumOfRoads += 1

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

    def add_road_item(self, road_item):
        self.road_items.append(road_item)

    def get_road_items(self):
        return self.road_items

class RoadItem:
    def __init__(self, mile_marker):
        self.mile_marker = mile_marker

    def get_mile_marker(self):
        return self.mile_marker

    def set_mile_marker(self, mile_marker):
        self.mile_marker = mile_marker

    def print_road_item(self):
        pass

    def update(self, seconds_passed):
        pass



class Dynamic(RoadItem, ABC):
    def __init__(self,mile_marker,current_road = None):
        super().__init__(mile_marker)
        self.mile_marker = mile_marker
        self.current_road = current_road
    

    def update(self, seconds: int):
        pass

        
class Static(RoadItem):
    def __init__(self):
        super().__init__()



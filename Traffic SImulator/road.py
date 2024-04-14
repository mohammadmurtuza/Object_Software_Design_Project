from enum import Enum
from abc import ABC,abstractmethod
# Heading enum translated from C#
class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

# Updated Road class integrating both existing and translated features
class Road:
    NumOfRoads = 0  # Static variable from translated code

    def __init__(self, name, locX=None, locY=None, len=None, hdg=None):
        self.name = name
        self.length = len
        self.heading = hdg
        self.xlocation = locX
        self.ylocation = locY
        Road.NumOfRoads += 1
        # Translated and commented out the initialization of head as it's part of the commented-out logic
        # self.head = RoadItem()
        # self.head.set_previous(None)
        # self.head.set_next(None)

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

    def add_roaditem(self, roaditem):
        print(f"Road item added: {roaditem}")

    def print(self, print_driver, obj):
        print_driver.print_road(self, obj)

    # Translated and commented-out methods related to RoadItem handling
    # def add_road_item(self, road_item):
    #     road_item.set_current_road(self)
    #     current_item = self.head
    #     while current_item.get_next() is not None:
    #         current_item = current_item.get_next()
    #         if current_item.get_mile_marker() > road_item.get_mile_marker():
    #             self.insert_new_item_before(current_item, road_item)
    #             return
    #     self.insert_new_item_after(current_item, road_item)

    # def insert_new_item_before(self, current, new_item):
    #     new_item.set_previous(current.get_previous())
    #     new_item.set_next(current)
    #     current.set_previous(new_item)
    #     if new_item.get_previous() is not None:
    #         new_item.get_previous().set_next(new_item)

    # def insert_new_item_after(self, current, new_item):
    #     new_item.set_next(current.get_next())
    #     current.set_next(new_item)
    #     new_item.set_previous(current)
    #     if new_item.get_next() is not None:
    #         new_item.get_next().set_previous(new_item)

# Preserving the existing RoadItem class
class RoadItem:
    def __init__(self,mile_marker,current_road = None):
        self.mile_marker = mile_marker
        self.current_road = current_road
        self.next_item = None
        self.prev_item = None

    def get_mile_marker(self):
        return self.mile_marker

    def GetCurrentRoad(self):
        return self.currentRoad

    def SetCurrentRoad(self, road):
        self.currentRoad = road

    def GetPrevious(self):
        return self.previtem

    def SetPrevious(self, item):
        self.previtem = item

    def GetNext(self):
        return self.nextitem

    def SetNext(self, item):
        self.nextitem = item


class Dynamic(RoadItem, ABC):
    def __init__(self,mile_marker,current_road = None):
        super().__init__(mile_marker)
        self.mile_marker = mile_marker
        self.current_road = current_road
    
    @abstractmethod

    def update(self, seconds: int):
        pass

        
class Static(RoadItem):
    def __init__(self):
        super().__init__()



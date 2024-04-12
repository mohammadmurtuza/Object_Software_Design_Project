from enum import Enum
from traffic_controls import TrafficLight


class Heading(Enum):
    North = 1
    South = 2
    East = 3
    West = 4

class RoadItem:
    def __init__(self):
        self.mile_marker = None
        self.current_road = None
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


class Dynamic(RoadItem):
    def __init__(self):
        super().__init__()
        self.upDate = 0
    
    def update(self):
        # Define the update logic for dynamic road items here
        pass

        
class Static(RoadItem):
    def __init__(self):
        super().__init__()

class Road:
    NumOfRoads = 0

    def __init__(self, name, locX=None, locY=None, length=0.180, heading=None):
        self.name = name
        self.length = length
        self.heading = heading
        self.xlocation = locX
        self.ylocation = locY
        self.road_items = []

        # Add two traffic lights about a third and two thirds through the road
        third = length // 3
        two_thirds = length * 2 // 3

        # Traffic light at about a third through the road
        self.add_traffic_light(red_duration=5, yellow_duration=3, green_duration=5, starting_color="red", mile_marker=third, location=third)
        
        # Traffic light at about two thirds through the road
        self.add_traffic_light(red_duration=5, yellow_duration=3, green_duration=5, starting_color="red", mile_marker=two_thirds, location=two_thirds)

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
        self.road_items.append(roaditem)

    def print(self, print_driver, obj):
        print_driver.print_road(self, obj)

    def PrintRoad(self):
        for item in self.road_items:
            item.PrintRoadItem()

    def add_traffic_light(self, red_duration, yellow_duration, green_duration, starting_color, mile_marker):
        traffic_light = TrafficLight(red_duration, yellow_duration, green_duration, starting_color, mile_marker)



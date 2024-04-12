from abc import ABC, abstractmethod
import numpy as np

from common import Conversions
from constants import Constants
from road import Heading  # Assuming use of numpy for multidimensional arrays
from traffic_controls import TrafficLight
class CharMatrix:
    def __init__(self, char_map_size):
        self.map = np.full((char_map_size, char_map_size), ' ', dtype=str)

class IPrintDriver(ABC):
    @abstractmethod
    def print_road(self, road, obj):
        pass

    @abstractmethod
    def print_car(self, car, obj):
        pass

class ConsolePrint(IPrintDriver):
    def print_road(self, road, obj):
        cm = obj
        CCx = Conversions.wc_point_to_cc_point(road.get_xlocation())
        CCy = Conversions.wc_point_to_cc_point(-road.get_ylocation())
        distance = 0
        CCRoadLength = Conversions.wc_length_to_cc_length(road.get_length())

        # Existing code for printing the road...

        


        if road.get_heading() == Heading.North:
            x = int(CCx)
            if 0 <= x < Constants.CharMapSize:
                while distance < CCRoadLength:
                    y = int(CCy - distance)
                    if 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = '|'
                        cm.map[y][x + 2] = '|'
                        cm.map[y][x + 4] = '|'
                    distance += 1
        elif road.get_heading() == Heading.East:
            y = int(CCy)
            if 0 <= y < Constants.CharMapSize:
                while distance < CCRoadLength:
                    x = int(CCx + distance)
                    if 0 <= x < Constants.CharMapSize:
                        cm.map[y][x] = '-'
                        cm.map[y + 2][x] = '-'
                        cm.map[y + 4][x] = '-'
                    distance += 1
        elif road.get_heading() == Heading.South:
            x = int(CCx)
            if 0 <= x < Constants.CharMapSize:
                while distance < CCRoadLength:
                    y = int(CCy + distance)
                    if 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = '|'
                        cm.map[y][x + 2] = '|'
                        cm.map[y][x + 4] = '|'
                    distance += 1
        elif road.get_heading() == Heading.West:
            y = int(CCy)
            if 0 <= y < Constants.CharMapSize:
                while distance < CCRoadLength:
                    x = int(CCx - distance)
                    if 0 <= x < Constants.CharMapSize:
                        cm.map[y][x] = '-'
                        cm.map[y + 2][x] = '-'
                        cm.map[y + 4][x] = '-'
                    distance += 1
        # Print traffic lights on the road
        for item in road.road_items:
            if isinstance(item, TrafficLight):
                if road.get_heading() == Heading.North or road.get_heading() == Heading.South:
                    x = int(CCx)
                    y = int(CCy + item.mile_marker)
                    if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = item.get_display_char()
                elif road.get_heading() == Heading.East or road.get_heading() == Heading.West:
                    x = int(CCx + item.mile_marker)
                    y = int(CCy)
                    if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = item.get_display_char()
        # Similar implementation for other headings...

    def print_car(self, car, obj):
        pass  # Implementation depends on Car class structure and how it's represented in CharMatrix

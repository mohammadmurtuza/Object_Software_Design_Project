from abc import ABC, abstractmethod
import numpy as np
from time import sleep

from common import Conversions
from constants import Constants
from road import Heading  # Assuming use of numpy for multidimensional arrays

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
    # def __init__(self):
    #     self.traffic_lights = {(30, 30): 'X', (30, 10): 'X'}
    #     self.light_states = {'X': ('red', 5), '-': ('yellow', 3), 'O': ('green', 5)}
    #     self.current_state = {pos: 'X' for pos in self.traffic_lights}

    def print_road(self, road, obj):
        cm = obj
        CCx = Conversions.wc_point_to_cc_point(road.get_xlocation())
        CCy = Conversions.wc_point_to_cc_point(-road.get_ylocation())
        distance = 0
        CCRoadLength = Conversions.wc_length_to_cc_length(road.get_length())

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
                    
        # Draw traffic lights at specified positions
    #     for position, state in self.traffic_lights.items():
    #         x, y = position
    #         if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
    #             cm.map[y][x] = state

    # def update_lights(self):
    #     while True:
    #         for position, (state, duration) in self.light_states.items():
    #             self.current_state[position] = state
    #             self.traffic_lights[position] = state  # Update current state
    #             sleep(duration)
    #             next_state = {'red': '-', 'yellow': 'O', 'green': 'X'}
    #             self.current_state[position] = next_state[state]
    #             self.traffic_lights[position] = next_state[state]


    def print_car(self, car, obj):
        pass  # Implementation depends on Car class structure and how it's represented in CharMatrix

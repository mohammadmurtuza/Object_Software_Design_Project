import os
import time
import numpy as np
from abc import ABC, abstractmethod

class Conversions:
    @staticmethod
    def wc_point_to_cc_point(val):
        from constants import Constants 
        return int(val * (Constants.CharMapSize / Constants.WorldSize) + (Constants.CharMapSize / 2))

    @staticmethod
    def wc_length_to_cc_length(val):
        from constants import Constants 
        return int(val * (Constants.CharMapSize / Constants.WorldSize))

class Constants:
    CharMapSize = 40
    WorldSize = 200

class Heading:
    North = 'North'
    East = 'East'
    South = 'South'
    West = 'West'

class CharMatrix:
    def __init__(self, char_map_size):
        self.map = np.full((char_map_size, char_map_size), ' ', dtype=str)

class IPrintDriver(ABC):
    @abstractmethod
    def print_road(self, road, obj):
        pass

class ConsolePrint(IPrintDriver):
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
        
        # # Print road items on the road
        # for road_item in road.road_items:
        #     if road.get_heading() == Heading.North or road.get_heading() == Heading.South:
        #         x = int(CCx)
        #         y = int(CCy + road_item.position)
        #         if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
        #             cm.map[y][x] = road_item.get_display_char()
        #     elif road.get_heading() == Heading.East or road.get_heading() == Heading.West:
        #         x = int(CCx + road_item.position)
        #         y = int(CCy)
        #         if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
        #             cm.map[y][x] = road_item.get_display_char()

        # Print traffic lights on the right side of the road at mile marker position
                    
        for road_item in road.road_items:
            if isinstance(road_item, TrafficLight):
                if road.get_heading() == Heading.North:
                    x = int(CCx + 6)  # Adjust horizontal position
                    y = int(CCy + road_item.position)
                    if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = road_item.get_display_char()
                elif road.get_heading() == Heading.East:
                    x = int(CCx + road_item.position)
                    y = int(CCy - 6)  # Adjust vertical position
                    if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = road_item.get_display_char()
                elif road.get_heading() == Heading.South:
                    x = int(CCx - 6)  # Adjust horizontal position
                    y = int(CCy + road_item.position)
                    if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = road_item.get_display_char()
                elif road.get_heading() == Heading.West:
                    x = int(CCx + road_item.position)
                    y = int(CCy + 6)  # Adjust vertical position
                    if 0 <= x < Constants.CharMapSize and 0 <= y < Constants.CharMapSize:
                        cm.map[y][x] = road_item.get_display_char()


class RoadItem:
    def __init__(self, position):
        self.position = position

    def get_display_char(self):
        return 'I'

class TrafficLight(RoadItem):
    def __init__(self, red_duration, yellow_duration, green_duration, start_color, position):
        super().__init__(position)
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.state = start_color
        self.last_change = time.time()

    def update(self, seconds_passed):
        current_time = time.time()
        if self.state == 'red' and current_time - self.last_change >= self.red_duration:
            self.state = 'green'
            self.last_change = current_time
        elif self.state == 'green' and current_time - self.last_change >= self.green_duration:
            self.state = 'yellow'
            self.last_change = current_time
        elif self.state == 'yellow' and current_time - self.last_change >= self.yellow_duration:
            self.state = 'red'
            self.last_change = current_time

    def get_display_char(self):
        if self.state == 'red':
            return 'X'
        elif self.state == 'green':
            return 'O'
        elif self.state == 'yellow':
            return '-'

class Road:
    def __init__(self, length, x_location, y_location, heading):
        self.length = length
        self.x_location = x_location
        self.y_location = y_location
        self.heading = heading
        self.road_items = []

    
    def get_xlocation(self):
        return self.x_location

    def get_ylocation(self):
        return self.y_location

    def get_length(self):
        return self.length

    def get_heading(self):
        return self.heading
    
    def add_road_item(self, road_item):
        self.road_items.append(road_item)

    def update_lights(self, seconds_passed):
        for road_item in self.road_items:
            if isinstance(road_item, TrafficLight):
                road_item.update(seconds_passed)

class Simulation:
    def __init__(self):
        self.roads = []
        self.seconds_passed = 0

    def add_road(self, road):
        self.roads.append(road)

    def update(self):
        for road in self.roads:
            road.update_lights(self.seconds_passed)

    def print_map(self):
        char_matrix = CharMatrix(Constants.CharMapSize)
        print_driver = ConsolePrint()
        for road in self.roads:
            print_driver.print_road(road, char_matrix)
        self.display(char_matrix)

    def display(self, char_matrix):
        os.system('cls' if os.name == 'nt' else 'clear')
        for row in char_matrix.map:
            print(''.join(row))

    def start(self):
        while True:
            self.update()
            self.print_map()
            self.seconds_passed += 1
            time.sleep(1)

def main():
    simulation = Simulation()

   
    main_road = Road(80, 0,0, Heading.North)

   
    main_road.add_road_item(TrafficLight(5, 3, 5, 'red', -14))  # Adjust position as per your requirement
    main_road.add_road_item(TrafficLight(5, 3, 5, 'red', -1))  # Adjust position as per your requirement

    simulation.add_road(main_road)


    simulation.start()

if __name__ == "__main__":
    main()


import os
import time
from conversions import *
from sui import *

class Simulation:
    def __init__(self):
        self.roads = []
        self.seconds_passed = 0

    # Remaining methods remain the same
    def add_road(self, road):
        self.roads.append(road)

    def update(self):
        for road in self.roads:
            road.update_lights(self.seconds_passed)

    def print(self, print_driver, obj):
        for road in self.roads:
            road.print(print_driver, obj)

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


    


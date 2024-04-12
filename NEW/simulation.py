from abc import ABC, abstractmethod
import time
import os
from road import *
from simulation import *
from gui import *
from constants import Constants
from gui import *
from map import *
from sui import *
from road import *

class Simulation:
    def __init__(self):
        self.dynamic_items = []
        self.roads = [] 
        self.simInput = MetricGUI()
        self.Uptown = self.simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)
        self.cm = CharMatrix(Constants.CharMapSize)
        self.map_obj = Map()
        self.map_obj.add_road(self.Uptown)
        self.cp = ConsolePrint()
        self.seconds_passed = 0

    def add_road(self, road):
        self.roads.append(road)

    def update(self):
        for road in self.roads:
            road.update_lights(self.seconds_passed)

    def print_map(self):
        self.clear_screen()
        for road in self.roads:
            road.PrintRoad()
        for i in range(Constants.CharMapSize):
            print("".join(self.cm.map[i]))

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

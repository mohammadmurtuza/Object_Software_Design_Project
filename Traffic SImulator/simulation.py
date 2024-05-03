# simulation.py
from traffic_controls import *
from sui import *
import os
import platform

from typing import List

class Simulation:
    def __init__(self, road_items: List[RoadItem]):
        self.road_items = road_items

    def update_lights(self, seconds_passed):
        for road_item in self.road_items:
            road_item.update(seconds_passed)

   
    @staticmethod
    def Art():
        print('''                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                              
eeeee eeeee  eeeee eeee eeee e  eeee    eeeee e  eeeeeee e   e e     eeeee eeeee eeeee eeeee  
  8   8   8  8   8 8    8    8  8  8    8   " 8  8  8  8 8   8 8     8   8   8   8  88 8   8  
  8e  8eee8e 8eee8 8eee 8eee 8e 8e      8eeee 8e 8e 8  8 8e  8 8e    8eee8   8e  8   8 8eee8e 
  88  88   8 88  8 88   88   88 88         88 88 88 8  8 88  8 88    88  8   88  8   8 88   8 
  88  88   8 88  8 88   88   88 88e8    8ee88 88 88 8  8 88ee8 88eee 88  8   88  8eee8 88   8                                                                                                                                                                                                                                                                                                                               
  ----------------------------------------------------------------------------------------------------
X : Red
- : Yellow
O : Green''')

    def update(self):
        print("Simulation updated")

    def add_dynamic_road_item(self, dynamic_road_item):
        print(f"Dynamic road item added: {dynamic_road_item}")
    
    def print_speed(self, vehicle):
        sim_output = self.gui.get_speed(vehicle)
        print(f"{vehicle.__class__.__name__} speed: {sim_output}")
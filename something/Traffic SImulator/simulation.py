# simulation.py
from traffic_controls import *
from sui import *
import os
import platform
class Simulation:
    def __init__(self,):
        self.roaditems = []
    @staticmethod

    def print_lights(traffic_lights, char_matrix):
        row_indices = [len(char_matrix.map) - 10, len(char_matrix.map) - 29]  # Calculate row indices

        for i, tl in enumerate(traffic_lights):
            symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[tl.current_color]
            char_matrix.map[row_indices[i]][tl.mile_marker] = symbol

    @staticmethod
    def clear_screen():
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")
    
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
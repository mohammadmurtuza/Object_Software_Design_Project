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
        # 第一个信号灯的行索引
        first_tl_row_index = len(char_matrix.map) - 13
        # 第二个信号灯的行索引应该比第一个信号灯的行索引小 13
        second_tl_row_index = first_tl_row_index - 13

        # 打印第一个信号灯
        symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[traffic_lights[0].current_color]
        char_matrix.map[first_tl_row_index][traffic_lights[0].mile_marker] = symbol

        # 打印第二个信号灯
        symbol = {'green': 'O','red': 'X', 'yellow': '-' }[traffic_lights[1].current_color]
        char_matrix.map[second_tl_row_index][traffic_lights[1].mile_marker] = symbol
    # def print_lights(traffic_lights, char_matrix):
    #     row_indices = [len(char_matrix.map) - 10, len(char_matrix.map) - 29]  # Calculate row indices

    #     for i, tl in enumerate(traffic_lights):
    #         symbol = {'red': 'X', 'yellow': '-', 'green': 'O'}[tl.current_color]
    #         char_matrix.map[row_indices[i]][tl.mile_marker] = symbol

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
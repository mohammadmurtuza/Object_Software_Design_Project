from time import sleep
import os
from simulation import *

class Timer:
    sim = None

    def __init__(self, this_sim):
        Timer.sim = this_sim

    def start_timer(self, map_obj, char_matrix, print_driver, time):
    
        for i in range(time):
            
            sleep(1)


            if platform.system() == "Windows":
                os.system("cls")
            else:
                os.system("clear")


            map_obj.print_map(print_driver, char_matrix)
            Simulation.Art()
            for row in char_matrix.map:
                print(''.join(row))
                

            Timer.sim.update_lights(1)
       
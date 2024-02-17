# simulation.py
from vehicles import Vehicle
from abc import ABC, abstractmethod
from gui import GUI  # Import the abstract GUI base class

class Simulation:
    def __init__(self, gui: GUI):
        self.roaditems = []
        self.gui = gui

    def update(self):
        print("Simulation updated")

    def add_dynamic_road_item(self, dynamic_road_item):
        print(f"Dynamic road item added: {dynamic_road_item}")
    
    def print_speed(self, vehicle):
        sim_output = self.gui.get_speed(vehicle)
        print(f"{vehicle.__class__.__name__} speed: {sim_output}")
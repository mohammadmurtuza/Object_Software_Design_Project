# simulation.py
from vehicles import Vehicle
from abc import ABC, abstractmethod

class ISimOutput(ABC):
    @abstractmethod
    def get_speed(self, vehicle):
        pass

class MetricOutput(ISimOutput):
    def get_speed(self, vehicle):
        return f"{round(vehicle.get_current_speed() * 1.6,2)} km/h."

class ImperialOutput(ISimOutput):
    def get_speed(self, vehicle):
        return f"{round(vehicle.get_current_speed(),2)} mph."

class Simulation:
    def __init__(self, output_type):
        self.roaditems = []
        self.output_type = output_type

    def update(self):
        print("Simulation updated")

    def add_dynamic_road_item(self, dynamic_road_item):
        print(f"Dynamic road item added: {dynamic_road_item}")
    
    def print_speed(self, vehicle):
        sim_output = self.output_type.get_speed(vehicle)
        print(f"{vehicle.__class__.__name__} speed: {sim_output}")


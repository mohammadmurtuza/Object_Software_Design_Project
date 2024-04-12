# simulation.py
from gui import GUI  # Import the abstract GUI base class
from traffic_light import TrafficLight  # Import the TrafficLight class

class Simulation:
    def __init__(self, gui: GUI):
        self.roaditems = []
        self.gui = gui
        self.traffic_lights = []  # List to hold traffic lights

    def update(self):
        print("Simulation updated")
        # Update traffic lights
        for light in self.traffic_lights:
            light.update()

    def add_dynamic_road_item(self, dynamic_road_item):
        print(f"Dynamic road item added: {dynamic_road_item}")

    def print_speed(self, vehicle):
        sim_output = self.gui.get_speed(vehicle)
        print(f"{vehicle.__class__.__name__} speed: {sim_output}")

    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

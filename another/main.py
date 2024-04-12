import os
import time
from simulation import Simulation
from road import Road
from traffic_light import TrafficLight
from conversions import *
from sui import *
from gui import *

def main():
    simulation = Simulation()

    # Create roads
    main_road = MetricGUI()

    # Add traffic lights to the main road
    Uptown = main_road.create_road("Uptown", 0.0, -0.09, .180, Heading.North)

    # Create a CharMatrix, Map, and ConsolePrint object
    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Simulation()
    map_obj.add_road(Uptown)
    cp = ConsolePrint()

    # Add the traffic lights to the simulation
    simulation = Simulation()
    for road in map_obj.roads:
        simulation.add_road(road)
        for item in road.road_items:
            if isinstance(item, TrafficLight):
                simulation.add_dynamic_item(item)

    # Start the simulation
    simulation.start()

if __name__ == "__main__":
    main()

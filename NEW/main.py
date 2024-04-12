# main.py
from simulation import *
from traffic_controls import *
from constants import Constants
from gui import *
from map import *
from sui import *
from road import *
from traffic_controls import TrafficLight

def main():
    # Create a MetricGUI object
    simInput = MetricGUI()

    # Create a road
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)

    # Create a CharMatrix, Map, and ConsolePrint object
    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    cp = ConsolePrint()

    # Add the traffic lights to the simulation
    simulation = Simulation()
    for road in map_obj.roads:
        simulation.add_road(road)
        for item in road.road_items:
            if isinstance(item, TrafficLight):
                simulation.add_dynamic_item(item)

    # Run the simulation
    simulation.run_simulation(10)

    # Print the map
    simulation.print_map()

if __name__ == "__main__":
    main()


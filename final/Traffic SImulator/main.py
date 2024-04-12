# main.py
from simulation import Simulation
from gui import MetricGUI  # Assuming you're using the MetricGUI class
from road import Road, Heading
from traffic_light import TrafficLight
from sui import *
from map import *
def main():
    simulation = Simulation(MetricGUI())

    # Create roads
    Uptown = Road("Uptown Road", 0.0, -0.09, 0.180, Heading.North)

    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    cp = ConsolePrint()
    map_obj.print(cp, cm)

    for i in range(Constants.CharMapSize):
        print("".join(cm.map[i]))

    # Add traffic lights to the Uptown road
    red_light_1 = TrafficLight(5, 3, 5, 'red', (30, 30))
    red_light_2 = TrafficLight(5, 3, 5, 'red', (30, 10))
    simulation.add_traffic_light(red_light_1)
    simulation.add_traffic_light(red_light_2)

    # Add roads to the simulation
    simulation.add_dynamic_road_item(Uptown)

    # Start the simulation


if __name__ == "__main__":
    main()

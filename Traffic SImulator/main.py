

from gui import MetricGUI
from map import Map
from simulation import Simulation
from sui import CharMatrix, ConsolePrint
from traffic_controls import TrafficLight
from timer import Timer
from sui import *


def main():

    gui = MetricGUI()
    map_obj = Map()
    cp = ConsolePrint()

    Uptown = gui.create_road("Uptown", 0.0, -0.09, 0.180, Heading.North)
    Uptown.add_road_item(TrafficLight(red_duration=5,yellow_duration= 3,green_duration= 5,start_color= 'red', mile_marker=10))
    Uptown.add_road_item(TrafficLight(red_duration=5, yellow_duration=3, green_duration=5, start_color='green',mile_marker= 31))
    map_obj.add_road(Uptown)

    cm = CharMatrix(Constants.CharMapSize)
    all_road_items = [road_item for road in map_obj.get_roads() for road_item in road.get_road_items()]
    simulation = Simulation(all_road_items)
    timer = Timer(simulation)


    timer.start_timer(map_obj, cm, cp, 20)

if __name__ == "__main__":
    main()

# main.py
from simulation import *
from vehicles import Car, Truck
from traffic_controls import *
from constants import Constants
from gui import *
from map import *
from sui import *
from simulation import *
from road import *
import time

def main():
    sim = Simulation()
    simInput = MetricGUI()

    # Road
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)

    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    cp = ConsolePrint() 
    map_obj.print(cp, cm)

    # Traffic Lights
    Uptown.add_road_item(TrafficLight(5, 3, 5, 'red', 6))
    Uptown.add_road_item(TrafficLight(5, 3, 5, 'red', 14))

    for i in range(20):
        sim.Art()

        for j in range(Constants.CharMapSize):
            print("".join(cm.map[j]))

        time.sleep(1)

        sim.clear_screen()

if __name__ == "__main__":
    main()

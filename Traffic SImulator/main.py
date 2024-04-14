# main.py
from simulation import *
from vehicles import Car, Truck
from traffic_controls import *
from constants import Constants
from gui import *
from map import *
from sui import *
from simulation import *
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
    tl1 = TrafficLight(mile_marker=18, red_duration=5, yellow_duration=3, green_duration=5)
    tl2 = TrafficLight(mile_marker=26, green_duration=5, yellow_duration=3, red_duration=3)
    traffic_lights = [tl1, tl2]

    for i in range(20):
        sim.Art()
        for tl in traffic_lights:
            tl.update()

        sim.print_lights(traffic_lights, cm)


        for j in range(Constants.CharMapSize):
            print("".join(cm.map[j]))

        time.sleep(1)

        sim.clear_screen()

if __name__ == "__main__":
    main()

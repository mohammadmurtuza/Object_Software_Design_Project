# main.py
from simulation import *
from vehicles import Car, Truck
from traffic_controls import *
from constants import Constants
from gui import *
from map import *
from sui import *
from threading import Thread

def main():
    simInput = MetricGUI()
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)

    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    cp = ConsolePrint()
    map_obj.print(cp, cm)

    # Start a separate thread to update traffic lights
    lights_thread = Thread(target=cp.update_lights)
    lights_thread.start()

    for i in range(Constants.CharMapSize):
        print("".join(cm.map[i]))

if __name__ == "__main__":
    main()

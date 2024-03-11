# main.py
from simulation import *
from vehicles import Car, Truck
from traffic_controls import SpeedLimit
from constants import Constants
from gui import *
from map import *
from sui import *
def main():
    # # User input for choosing the system
    # system_choice = input("Choose the system (M for Metric, I for Imperial): ").upper()
    # if system_choice == 'M':
    #     gui = MetricGUI()
    # else:
    #     gui = ImperialGUI()
    
    # # User input for speed limit...
    # speed_limit = float(input("Enter the speed limit: "))
    
    # # Initialize vehicles and set their desired speed using the GUI
    # car = Car()
    # gui.set_speed_limit(car, speed_limit)
    # truck1 = Truck(4)
    # gui.set_speed_limit(truck1, speed_limit)
    # truck2 = Truck(8)
    # gui.set_speed_limit(truck2, speed_limit)

    # vehicles = [car, truck1, truck2]

    # # Simulation loop
    # for _ in range(11):
    #     for v in vehicles:
    #         v.update_speed(1)
    #         print(f"{v.__class__.__name__} speed: {gui.get_speed(v)}")

# if __name__ == "__main__":
#     main()


    # # Create instances of vehicles and simulation
    # car_instance = Car()
    # car_instance.set_desired_speed(65.0)
    
    # truck_instance1 = Truck(4)
    # truck_instance1.set_desired_speed(55.0)
    
    # truck_instance2 = Truck(8)
    # truck_instance2.set_desired_speed(50.0)

    # simulation = Simulation()
    # simulation.Update()
    # simulation.AddDynamicRoadItem(car_instance)
    # simulation.AddDynamicRoadItem(truck_instance1)
    # simulation.AddDynamicRoadItem(truck_instance2)

    # speed_limit = SpeedLimit()
    # speed_limit.GetSpeedLimit()
# New simulation setup from C# Program.cs
    
    simInput = MetricGUI()
    Uptown = simInput.create_road("Uptown", 0.0, -0.09, .180, Heading.North)
    Crosstown = simInput.create_road("Crosstown", -0.09, 0.0, .180, Heading.East)

    # Corrected instantiation of CharMatrix
    cm = CharMatrix(Constants.CharMapSize)
    map_obj = Map()
    map_obj.add_road(Uptown)
    map_obj.add_road(Crosstown)
    cp = ConsolePrint()
    map_obj.print(cp, cm)

    for i in range(Constants.CharMapSize):
        print("".join(cm.map[i]))
if __name__ == "__main__":
    main()

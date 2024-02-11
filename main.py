# main.py
from simulation import *
from vehicles import Car, Truck
from traffic_controls import SpeedLimit
from constants import Constants


def main():

    sim_output = MetricOutput() #for Kilometer
    #OR
    # sim_output = ImperialOutput() #for Miles

    car = Car()
    car.set_desired_speed(65.0)
    truck1 = Truck(4)
    truck1.set_desired_speed(55.0)
    truck2 = Truck(8)
    truck2.set_desired_speed(50.0)
    vehicles = [car, truck1, truck2]

    simulation = Simulation(sim_output)

    for _ in range(11):
        for v in vehicles:
            v.update_speed(1)
            simulation.print_speed(v)

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

if __name__ == "__main__":
    main()

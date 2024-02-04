# program.py
from vehicles import Car, Truck
from constants import Constants
class Program:
    def main():
        car = Car()
        car.SetDesiredSpeed(65.0)
        truck1 = Truck(4)
        truck1.SetDesiredSpeed(55.0)
        truck2 = Truck(8)
        truck2.SetDesiredSpeed(50.0)
        vehicles = [car, truck1, truck2]

        for _ in range(11):
            for v in vehicles:
                v.update_speed(1)
                s = v.__class__.__name__
                print(f"{s} speed: {v.GetCurrentSpeed():.2f} mph")

Program.main()
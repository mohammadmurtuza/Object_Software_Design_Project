# program.py
from vehicles import Car, Truck

class Program:
    @staticmethod
    def main():
        car = Car()
        car.set_desired_speed(65.0)
        truck1 = Truck(4)
        truck1.set_desired_speed(55.0)
        truck2 = Truck(8)
        truck2.set_desired_speed(50.0)
        vehicles = [car, truck1, truck2]
        for _ in range(11):
            for v in vehicles:
                v.update_speed(1)
                s = v.__class__.__name__
                print(f"{s} speed: {v.get_current_speed():.2f} mph")

Program.main()
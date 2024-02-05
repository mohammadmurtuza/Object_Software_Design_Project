class Constants:
    AccRate = 3.5  # Acceleration rate for cars in m/s
    AccRateEmpty = 2.5  # Acceleration rate for light trucks in m/s
    AccRateFull = 1.0  # Acceleration rate for heavy trucks in m/s
    DecRate = 7.0  # Braking rate for cars in m/s
    DecRateEmpty = 5.0  # Braking rate for light trucks in m/s
    DecRateFull = 2.0  # Braking rate for light trucks in m/s
    MpsToMph = 2.237

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

class Vehicle:
    def __init__(self):
        self.current_speed = 0.0
        self.desired_speed = 0.0

    def get_current_speed(self):
        return self.current_speed

    def set_desired_speed(self, mph):
        self.desired_speed = mph

    def set_current_speed(self, speed):
        if self.current_speed <= speed:  # accelerating
            if speed > self.desired_speed:
                self.current_speed = self.desired_speed
            else:
                self.current_speed = speed
        else:  # braking
            if speed < self.desired_speed:
                self.current_speed = self.desired_speed
            else:
                self.current_speed = speed

    def update_speed(self, seconds):
        if self.current_speed > self.desired_speed:
            self.decelerate(seconds)
        elif self.current_speed < self.desired_speed:
            self.accelerate(seconds)

    def accelerate(self, seconds_delta):
        pass

    def decelerate(self, seconds_delta):
        pass

class Car(Vehicle):
    def accelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() + Constants.AccRate * seconds_delta * Constants.MpsToMph)

    def decelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() - Constants.DecRate * seconds_delta * Constants.MpsToMph)

class Truck(Vehicle):
    def __init__(self, weight):
        super().__init__()
        self.load_weight = weight

    def accelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() + Constants.AccRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.set_current_speed(self.get_current_speed() + Constants.AccRateFull * seconds_delta * Constants.MpsToMph)

    def decelerate(self, seconds_delta):
        if self.load_weight <= 5:
            self.set_current_speed(self.get_current_speed() - Constants.DecRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.set_current_speed(self.get_current_speed() - Constants.DecRateFull * seconds_delta * Constants.MpsToMph)

# Run the main function
Program.main()

from road import Dynamic
from constants import Constants
from abc import ABC, abstractmethod

class Vehicle(Dynamic):
    def __init__(self):
        super().__init__()
        self.current_speed = 0
        self.desired_speed = 0
        self.speedLimit = 0
        self.color = None 
        self.currentDirection = 0
        self.currentLocation = (0, 0)
        

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
      
    @abstractmethod
    def accelerate(self, seconds_delta):
        pass


    @abstractmethod
    def decelerate(self, seconds_delta):
        pass


    def Turn(self, direction, degrees):
        #print(f"Turning {direction} {degrees}°") # for debugging purposes
        pass


class Car(Vehicle):
    def __init__(self):
        super().__init__() #The super() function is used to give access to methods and properties of a parent or sibling class.

    def accelerate(self, seconds_delta):
        # Acceleration now directly uses m/s without conversion
        self.set_current_speed(self.get_current_speed() + Constants.AccRate * seconds_delta)

    def decelerate(self, seconds_delta):
        # Deceleration now directly uses m/s without conversion
        self.set_current_speed(self.get_current_speed() - Constants.DecRate * seconds_delta)


class Truck(Vehicle):
    def __init__(self,weight):
        super().__init__()
        self.loadWeight = weight

    def SetLoadWeight(self, weight):
        #print(f"Setting Truck load to {weight} lbs.") # for debugging purposes
        pass

    def accelerate(self, seconds_delta):
        # Accelerate based on load weight without conversion
        acc_rate = Constants.AccRateEmpty if self.loadWeight <= 5 else Constants.AccRateFull
        self.set_current_speed(self.get_current_speed() + acc_rate * seconds_delta)

    def decelerate(self, seconds_delta):
        # Decelerate based on load weight without conversion
        dec_rate = Constants.DecRateEmpty if self.loadWeight <= 5 else Constants.DecRateFull
        self.set_current_speed(self.get_current_speed() - dec_rate * seconds_delta)




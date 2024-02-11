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
        self.set_current_speed(self.get_current_speed() + Constants.AccRate * seconds_delta * Constants.MpsToMph)

    def decelerate(self, seconds_delta):
        self.set_current_speed(self.get_current_speed() - Constants.DecRate * seconds_delta * Constants.MpsToMph)

class Truck(Vehicle):
    def __init__(self,weight):
        super().__init__()
        self.loadWeight = weight

    def SetLoadWeight(self, weight):
        #print(f"Setting Truck load to {weight} lbs.") # for debugging purposes
        pass

    def accelerate(self, seconds_delta):
        if self.loadWeight <= 5:
            self.set_current_speed(self.get_current_speed() + Constants.AccRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.set_current_speed(self.get_current_speed() + Constants.AccRateFull * seconds_delta * Constants.MpsToMph)

    def decelerate(self, seconds_delta):
        if self.loadWeight <= 5:
            self.set_current_speed(self.get_current_speed() - Constants.DecRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.set_current_speed(self.get_current_speed() - Constants.DecRateFull * seconds_delta * Constants.MpsToMph)




from road import Dynamic
from constants import Constants


class Vehicle(Dynamic):
    def __init__(self):
        super().__init__()
        self.current_speed = 0
        self.desired_speed = 0
        self.speedLimit = 0
        self.color = None 
        self.currentDirection = 0
        self.currentLocation = (0, 0)

    def GetCurrentSpeed(self):
        #print(f"Current speed is {self.current_speed} mph.")
        return self.current_speed

    def SetDesiredSpeed(self, speed):
        self.desiredSpeed = speed
        #print(f"Setting desired speed to {speed} mph.")
    
    def SetCurrentSpeed(self, speed):
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
            self.Decelerate(seconds)
        elif self.current_speed < self.desired_speed:
            self.Accelerate(seconds)

    def Accelerate(self, toSpeed):
        #print(f"Accelerating to {toSpeed} mph.") # for debugging purposes
        pass

    def Decelerate(self, toSpeed):
        #print(f"Decelerating to {toSpeed} mph.") # for debugging purposes
        pass

    def Turn(self, direction, degrees):
        #print(f"Turning {direction} {degrees}°") # for debugging purposes
        pass


class Car(Vehicle):
    def __init__(self):
        super().__init__() #The super() function is used to give access to methods and properties of a parent or sibling class.
    def Accelerate(self, seconds_delta):
        self.SetCurrentSpeed(self.GetCurrentSpeed() + Constants.AccRate * seconds_delta * Constants.MpsToMph)

    def Decelerate(self, seconds_delta):
        self.SetCurrentSpeed(self.GetCurrentSpeed() - Constants.DecRate * seconds_delta * Constants.MpsToMph)
class Truck(Vehicle):
    def __init__(self,weight):
        super().__init__()
        self.loadWeight = weight

    def SetLoadWeight(self, weight):
        #print(f"Setting Truck load to {weight} lbs.") # for debugging purposes
        pass

    def Accelerate(self, seconds_delta):
        if self.loadWeight <= 5:
            self.SetCurrentSpeed(self.GetCurrentSpeed() + Constants.AccRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.SetCurrentSpeed(self.GetCurrentSpeed() + Constants.AccRateFull * seconds_delta * Constants.MpsToMph)

    def Decelerate(self, seconds_delta):
        if self.loadWeight <= 5:
            self.SetCurrentSpeed(self.GetCurrentSpeed() - Constants.DecRateEmpty * seconds_delta * Constants.MpsToMph)
        else:
            self.SetCurrentSpeed(self.GetCurrentSpeed() - Constants.DecRateFull * seconds_delta * Constants.MpsToMph)




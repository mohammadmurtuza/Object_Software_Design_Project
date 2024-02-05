'''Mohammad Murtuza'''
class Road:
    def __init__(self, name):
        self.name = name
        self.length = None
        self.head = None  

    def GetLength(self):
        return self.length

    def GetRoadName(self):
        return self.name

    def AddRoaditem(self, roaditem):
        print(f"Road item added: {roaditem}")

class RoadItem:
    def __init__(self):
        self.mileMarker = None
        self.currentRoad = None  
        self.nextitem = None  
        self.previtem = None  

    def GetMileMarker(self):
        return self.mileMarker

    def GetCurrentRoad(self):
        return self.currentRoad

    def SetCurrentRoad(self, road):
        self.currentRoad = road

    def GetPrevious(self):
        return self.previtem

    def SetPrevious(self, item):
        self.previtem = item

    def GetNext(self):
        return self.nextitem

    def SetNext(self, item):
        self.nextitem = item


class Simulation:
    def __init__(self):
        self.roaditems = []

    def Update(self):
        print("Simulation updated")

    def AddDynamicRoadItem(self,dynamicroaditem):
        print(f"Dynamic road item added: {dynamicroaditem}")

class Dynamic(RoadItem):
    def __init__(self):
        super().__init__()
        self.upDate = 0

class Light(Dynamic):
    def __init__(self):
        super().__init__()
        self.redTime = 0
        self.yellowTime = 0
        self.greenTime = 0
        self.lit = 0
        self.timeOn = 0

    def update(self, seconds):
        return seconds

    def getLightColor(self, color):
        pass


class Vehicle(Dynamic):
    def __init__(self):
        super().__init__()
        self.currentSpeed = 70
        self.desiredSpeed = 0
        self.speedLimit = 0
        self.color = None 
        self.currentDirection = 0
        self.currentLocation = (0, 0)

    def GetCurrentSpeed(self):
        print(f"Current speed is {self.currentSpeed} mph.")
        return self.currentSpeed

    def SetDesiredSpeed(self, speed):
        self.desiredSpeed = speed
        print(f"Setting desired speed to {speed} mph.")

    def Accelerate(self, toSpeed):
        print(f"Accelerating to {toSpeed} mph.") # for debugging purposes
        pass

    def Decelerate(self, toSpeed):
        print(f"Decelerating to {toSpeed} mph.") # for debugging purposes
        pass

    def Turn(self, direction, degrees):
        print(f"Turning {direction} {degrees}°") # for debugging purposes
        pass


class Car(Vehicle):
    def __init__(self):
        super().__init__() #The super() function is used to give access to methods and properties of a parent or sibling class.


class Truck(Vehicle):
    def __init__(self):
        super().__init__()
        self.loadWeight = 0

    def SetLoadWeight(self, weight):
        print(f"Setting Truck load to {weight} lbs.") # for debugging purposes
        pass

class Static(RoadItem):
    def __init__(self):
        super().__init__()

class StopSign(Static):
    def __init__(self):
        super().__init__()

class Intersection(Static):
    def __init__(self):
        super().__init__()
        self.turns = []

    def GetTurns(self):
        return self.turns

    def AddTurn(self, turn):
        self.turns.append(turn)
        print(f"Turn added: {turn}")

    def GetTurn(self, index):
        try:
            return self.turns[index]
        except IndexError:
            raise ValueError("Invalid turn index")
    

class SpeedLimit(Static):
    def __init__(self):
        super().__init__()
        self.speedLimit = 45

    def GetSpeedLimit(self):
        print(f"Speed Limit:{self.speedLimit}")
        return self.speedLimit

class Yield(Static):
    def __init__(self):
        super().__init__()
    

# Debugging and testing code
car_instance = Car()
car_instance.Accelerate(85)
car_instance.Turn("left", 90)
car_instance.GetCurrentSpeed()

truck_instance = Truck()
truck_instance.Decelerate(35)
truck_instance.SetLoadWeight(2000)
truck_instance.SetDesiredSpeed(55)

simulation = Simulation()
simulation.Update()
simulation.AddDynamicRoadItem(car_instance)
simulation.AddDynamicRoadItem(truck_instance)

speed_limit = SpeedLimit()
speed_limit.GetSpeedLimit()

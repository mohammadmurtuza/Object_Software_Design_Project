
from vehicles import Car, Truck


class Simulation:
    def __init__(self):
        self.roaditems = []

    def Update(self):
        print("Simulation updated")

    def AddDynamicRoadItem(self,dynamicroaditem):
        print(f"Dynamic road item added: {dynamicroaditem}")
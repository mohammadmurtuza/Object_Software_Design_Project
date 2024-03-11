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


class Dynamic(RoadItem):
    def __init__(self):
        super().__init__()
        self.upDate = 0

        
class Static(RoadItem):
    def __init__(self):
        super().__init__()



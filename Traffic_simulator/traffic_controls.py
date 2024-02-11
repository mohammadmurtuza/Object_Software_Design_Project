from road import Dynamic, Static

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
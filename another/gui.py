from abc import ABC, abstractmethod
from road import *
from conversions import *

class GUI( ABC):

    @abstractmethod
    def create_road(self, name, locx, locy, len, hdg):
        pass

class MetricGUI(GUI):

    def create_road(self, name, locx, locy, len, hdg):
        # Implementation based on Metric system from C# MetricGUI
        return Road(name, locx / Constants.MetersToKm, locy / Constants.MetersToKm, len / Constants.MetersToKm, hdg)

class ImperialGUI(GUI):

    def create_road(self, name, locx, locy, len, hdg):
        # Implementation based on Imperial system from C# ImperialGUI
        return Road(name, locx / Constants.MetersToMiles, locy / Constants.MetersToMiles, len / Constants.MetersToMiles, hdg)

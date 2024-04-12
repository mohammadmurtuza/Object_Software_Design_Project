# gui.py
from abc import ABC, abstractmethod
from constants import Constants
from road import Road


class GUI(ABC):


    @abstractmethod
    def create_road(self, name, locx, locy, len, hdg):
        pass

class MetricGUI(GUI):

    def create_road(self, name, locx, locy, len, hdg):
        return Road(name, locx / Constants.MetersToKm, locy / Constants.MetersToKm, len / Constants.MetersToKm, hdg)

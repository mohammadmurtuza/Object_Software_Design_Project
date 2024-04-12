from abc import ABC, abstractmethod
from constants import Constants
from vehicles import Vehicle  # If the Vehicle class is needed for type annotations

class ISimOutput(ABC):
    @abstractmethod
    def get_speed(self, vehicle: Vehicle) -> float:
        pass

class ISimInput(ABC):
    @abstractmethod
    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        pass

class GUI(ISimInput, ISimOutput, ABC):
    @abstractmethod
    def get_speed(self, vehicle: Vehicle) -> float:
        pass

    @abstractmethod
    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        pass

class MetricGUI(GUI):
    def get_speed(self, vehicle: Vehicle) -> float:
        # return vehicle.get_current_speed() * Constants.MpsToKph
        speed_kmh = vehicle.get_current_speed() * Constants.MpsToKph
        return f"{speed_kmh:.2f} Km/h"

    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        vehicle.set_desired_speed(speed / Constants.MpsToKph)

class ImperialGUI(GUI):
    def get_speed(self, vehicle: Vehicle) -> float:
        # return vehicle.get_current_speed() * Constants.MpsToMph
        speed_mph = vehicle.get_current_speed() * Constants.MpsToMph
        return f"{speed_mph:.2f} mph"

    def set_speed_limit(self, vehicle: Vehicle, speed: float) -> None:
        vehicle.set_desired_speed(speed / Constants.MpsToMph)

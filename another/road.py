from traffic_light import TrafficLight

class Road:
    def __init__(self, name, length, x_location, y_location, heading):
        self.length = length
        self.x_location = x_location
        self.y_location = y_location
        self.heading = heading
        self.traffic_lights = []

    # Remaining methods remain the same
    def add_traffic_light(self, traffic_light):
        self.traffic_lights.append(traffic_light)

    def get_xlocation(self):
        return self.x_location

    def get_ylocation(self):
        return self.y_location

    def get_length(self):
        return self.length

    def get_heading(self):
        return self.heading

    def update_lights(self, seconds_passed):
        for light in self.traffic_lights:
            light.update(seconds_passed)


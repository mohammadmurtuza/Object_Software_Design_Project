from road import Dynamic
import time
class TrafficLight(Dynamic):
    def __init__(self, mile_marker, red_duration, yellow_duration, green_duration, start_color='red'):
        super().__init__(mile_marker)
        self.mile_marker=mile_marker
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.current_color = start_color
        self.timer = 0  # Initialize timer to keep track of light changes

    def update(self, seconds=1):
        self.timer += seconds
        # Calculate the total duration of the traffic light cycle
        cycle_duration = self.red_duration + self.yellow_duration + self.green_duration
        # Using modulo to cycle through the light colors
        self.timer %= cycle_duration
        if self.timer <= self.red_duration:
            self.current_color = 'red'
        elif self.timer <= self.red_duration + self.green_duration:
            self.current_color = 'green'
        else:
            self.current_color = 'yellow'

    

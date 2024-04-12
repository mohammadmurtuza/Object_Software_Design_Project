
from road import *
import time

class TrafficLight:
    def __init__(self, red_duration, yellow_duration, green_duration, starting_color, mile_marker):
        self.red_duration = red_duration
        self.yellow_duration = yellow_duration
        self.green_duration = green_duration
        self.state = starting_color
        self.last_change = time.time()
        self.position = mile_marker

    def update(self):
        current_time = time.time()
        if self.state == 'red' and current_time - self.last_change >= self.red_duration:
            self.state = 'green'
            self.last_change = current_time
        elif self.state == 'green' and current_time - self.last_change >= self.green_duration:
            self.state = 'yellow'
            self.last_change = current_time
        elif self.state == 'yellow' and current_time - self.last_change >= self.yellow_duration:
            self.state = 'red'
            self.last_change = current_time


    def get_display_char(self):
        if self.state == 'red':
            return 'X'
        elif self.state == 'green':
            return 'O'
        elif self.state == 'yellow':
            return '-'



import random

class SolarPanel:
    def __init__(self, efficiency=0.8):
        self.efficiency = efficiency
        self.power_output = 0

    def generate_power(self, sunlight_intensity):
        self.power_output = sunlight_intensity * self.efficiency
        return self.power_output

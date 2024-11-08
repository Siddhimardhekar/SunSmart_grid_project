from solar import SolarPanel
from battery import Battery
from load import Load

class EnergyManagementSystem:
    def __init__(self, solar_panel, battery, load):
        self.solar_panel = solar_panel
        self.battery = battery
        self.load = load

    def distribute_energy(self, sunlight_intensity):
        solar_energy = self.solar_panel.generate_power(sunlight_intensity)
        load_demand = self.load.power_demand

        if solar_energy >= load_demand:
            # Supply load from solar and charge battery with excess
            self.battery.charge(solar_energy - load_demand)
        else:
            # Supply load with solar and battery
            energy_needed = load_demand - solar_energy
            self.battery.discharge(energy_needed)

from solar import SolarPanel
from battery import Battery
from load import Load
from ems import EnergyManagementSystem

# Create instances of each component
solar = SolarPanel()
battery = Battery()
load = Load(power_demand=200)  # Example load demand
ems = EnergyManagementSystem(solar, battery, load)

# Simulate sunlight intensity
sunlight_intensity = 500  # Example value for daytime sunlight

# Distribute energy to load
ems.distribute_energy(sunlight_intensity)

# Print battery level after energy distribution
print(f"Battery Level: {battery.charge_level} Wh")

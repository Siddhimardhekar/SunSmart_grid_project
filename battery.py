class Battery:
    def __init__(self, capacity=1000, charge_level=500):
        self.capacity = capacity
        self.charge_level = charge_level

    def charge(self, energy_input):
        self.charge_level = min(self.charge_level + energy_input, self.capacity)

    def discharge(self, energy_output):
        self.charge_level = max(self.charge_level - energy_output, 0)

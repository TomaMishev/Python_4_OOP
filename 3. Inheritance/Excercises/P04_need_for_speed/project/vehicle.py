class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        needed_km = self.DEFAULT_FUEL_CONSUMPTION * kilometers
        if self.fuel >= needed_km:
            self.fuel -= needed_km

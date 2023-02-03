from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTests(TestCase):
    def test_vehicle_init(self):
        fuel = 100
        hp = 150

        car = Vehicle(fuel, hp)

        self.assertEqual(100, car.fuel)
        self.assertEqual(150, car.horse_power)
        self.assertEqual(100, car.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, car.fuel_consumption)

    def test_vehicle_str_returns_proper_string(self):
        car = Vehicle(100, 150)
        result = str(car)
        expected_result = f"The vehicle has {car.horse_power} " \
                          f"horse power with {car.fuel} fuel left and {car.fuel_consumption} fuel consumption"
        self.assertEqual(expected_result, result)

    def test_drive_raises_when_distance_is_not_reachable(self):
        car = Vehicle(100, 150)
        with self.assertRaises(Exception) as ex:
            car.drive(car.fuel)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_reduces_fuel(self):
        car = Vehicle(100, 150)
        distance = 10
        burned_fuel = distance * car.fuel_consumption
        result = car.fuel - burned_fuel

        car.drive(distance)

        self.assertEqual(result, car.fuel)

    def test_refuel_raises_when_trunk_is_full(self):
        car = Vehicle(100, 150)
        with self.assertRaises(Exception) as ex:
            car.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_increases_vehicle_fuel(self):
        car = Vehicle(100, 150)
        car.fuel = 60

        car.refuel(20)

        self.assertEqual(80, car.fuel)





if __name__ == "__main__":
    main()

# Create a class WorkerTests
# In judge you need to submit just the WokerTests class, with the unittest module imported.
# Create the following tests:
# •	Test if the worker is initialized with the correct name, salary, and energy
# •	Test if the worker's energy is incremented after the rest method is called
# •	Test if an error is raised if the worker tries to work with negative energy or equal to 0
# •	Test if the worker's money is increased by his salary correctly after the work method is called
# •	Test if the worker's energy is decreased after the work method is called
# •	Test if the get_info method returns the proper string with correct values


class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'


from unittest import TestCase, main


class WorkerTests(TestCase):

    def test_worker_is_initialized_correctly(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual("Test", worker.name)
        self.assertEqual(100, worker.salary)
        self.assertEqual(10, worker.energy)
        self.assertEqual(0, worker.money)

    def test_energy_is_increased_after_rest(self):
        worker = Worker("Test", 100, 10)
        self.assertEqual(10, worker.energy)

        worker.rest()

        self.assertEqual(11, worker.energy)

    def test_worker_work_with_zero_energy_raises(self):
        worker = Worker("Test", 100, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_worker_with_negative_energy_raises(self):
        worker = Worker("Test", 100, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_increased_money_by_salary(self):
        worker = Worker("Test", 100, 10)

        self.assertEqual(0, worker.money)

        worker.work()

        self.assertEqual(100, worker.salary)

        worker.work()

        self.assertEqual(200, worker.money)

    def test_if_energy_is_decreased_after_work(self):
        worker = Worker("Test", 100, 10)

        worker.work()

        self.assertEqual(9, worker.energy)

    def test_if_get_info_return_proper_info(self):
        worker = Worker("Test", 100, 10)

        result = worker.get_info()

        self.assertEqual(f"{worker.name} has saved {worker.money} money.", result)





if __name__ == "__main__":
    main()

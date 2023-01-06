from P03_multiple_inheritance.employee import Employee
from P03_multiple_inheritance.person import Person


class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
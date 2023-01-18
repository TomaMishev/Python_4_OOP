from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:

    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = self.__get_sub_id(subscription_id)
        customer = self.__get_customer_id(subscription_id)
        trainer = self.__get_trainer_id(subscription_id)
        equipment = self.__get_equipment_id(subscription_id)
        plan = self.__get_plan(subscription_id)

        result = f"{subscription.__repr__()}\n" \
                 f"{customer.__repr__()}\n{trainer.__repr__()}\n" \
                 f"{equipment.__repr__()}\n{plan.__repr__()}"
        return result

    def __get_sub_id(self, subscription_id):
        for current in self.subscriptions:
            if current.id == subscription_id:
                return current

    def __get_customer_id(self, subscription_id):
        for current in self.customers:
            if current.id == subscription_id:
                return current

    def __get_trainer_id(self, subscription_id):
        for current in self.trainers:
            if current.id == subscription_id:
                return current

    def __get_equipment_id(self, subscription_id):
        for current in self.equipment:
            if current.id == subscription_id:
                return current

    def __get_plan(self, subscription_id):
        for current in self.plans:
            if current.id == subscription_id:
                return current


customer = Customer("John", "Maple Street", "john.smith@gmail.com")
equipment = Equipment("Treadmill")
trainer = Trainer("Peter")
subscription = Subscription("14.05.2020", 1, 1, 1)
plan = ExercisePlan(1, 1, 20)

gym = Gym()

gym.add_customer(customer)
gym.add_equipment(equipment)
gym.add_trainer(trainer)
gym.add_plan(plan)
gym.add_subscription(subscription)

print(Customer.get_next_id())

print(gym.subscription_info(1))

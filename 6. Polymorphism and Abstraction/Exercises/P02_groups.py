# Create a class called Person. Upon initialization, it will receive a name (str) and a surname (str). Implement the
# needed magic methods so that: •	Each person could be represented by their names, separated by a single space. •
# When you concatenate two people, you should return a new instance of a person who will take the first name from the
# first person and the surname from the second person. Create another class called Group. Upon initialization,
# it should receive a name (str) and people (list of Person instances). Implement the needed magic methods so that:
# •	When you access the length of a group instance, you should receive the total number of people in the group. •
# When you concatenate two groups, you should return a new instance of a group which will have a name -string in the
# format "{first_name} {second_name}" and all the people in the two groups will participate in the new one too. •
# Each group should be represented in the format "Group {name} with members {members' names separated by comma and
# space}" •	You could iterate over a group, and each person (element of the group) should be represented in the format
# "Person {index}: {person's name}"


class Person:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return Person(self.name, other.surname)


class Group:

    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, other):
        return Group(f"{self.name} {other.owner}", self.people + other.people)

    def __getitem__(self, idx):
        return f"Person {idx}: {str(self.people[idx])}"

    def __str__(self):
        return f"Group {self.name} with members {', '.join([str(x) for x in self.people])}"

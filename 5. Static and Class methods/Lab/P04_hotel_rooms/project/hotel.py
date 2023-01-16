from project.room import Room


class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []

    @property
    def guests(self):
        return sum([room.guests for room in self.rooms])

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [room for room in self.rooms if room_number == room.number][0]
        room.take_room(people)

    def free_room(self, room_number):
        room = [room for room in self.rooms if room_number == room.number][0]
        room.free_room()

    def status(self):
        free_rooms = [str(room.number) for room in self.rooms if not room.is_taken]
        taken_rooms = [str(room.number) for room in self.rooms if room.is_taken]
        result = f"Hotel {self.name} has {self.guests} total guests\n" \
                 f"Free rooms: {', '.join(free_rooms)}\n" \
                 f"Taken rooms: {', '.join(taken_rooms)}"
        return result


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

print(hotel.status())

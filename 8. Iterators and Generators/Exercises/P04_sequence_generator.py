# Create a class called sequence_repeat which should receive a sequence and a number upon initialization. Implement
# an iterator to return the given elements, so they form a string with a length - the given number. If the number is
# greater than the number of elements, then the sequence repeats as necessary

class sequence_repeat:
    def __init__(self, sequence, number):
        self.sequence = sequence
        self.number = number
        self.pointer = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.pointer == self.number:
            raise StopIteration
        symbol = self.sequence[self.pointer % len(self.sequence)]
        self.pointer += 1
        return symbol


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

# Create a class called take_skip. Upon initialization, it should receive a step (int) and a count (int). Implement
# the __iter__ and __next__ functions. The iterator should return the count numbers (starting from 0) with the given
# step. For more clarification.

class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.iters = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.iters == self.count:
            raise StopIteration
        current = self.iters * self.step
        self.iters += 1
        return current


numbers = take_skip(2, 6)
for number in numbers:
    print(number)

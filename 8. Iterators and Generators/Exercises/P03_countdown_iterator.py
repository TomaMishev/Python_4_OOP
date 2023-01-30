# Create a class called countdown_iterator. Upon initialization, it should receive a count. Implement the iterator to
# return each countdown number (from count to 0 inclusive), separated by a single space.

class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_iter = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_iter < 0:
            raise StopIteration
        result = self.current_iter
        self.current_iter -= 1
        return result


iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")

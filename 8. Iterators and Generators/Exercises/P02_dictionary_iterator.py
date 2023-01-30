# Create a class called dictionary_iter. Upon initialization, it should receive a dictionary object. Implement the
# iterator to return each key-value pair of the dictionary as a tuple of two elements (the key and the value).

class dictionary_iter:

    def __init__(self, obj):
        self.obj = list(obj.items())
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx >= len(self.obj):
            raise StopIteration
        current = self.obj[self.idx]
        self.idx += 1
        return current



result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)

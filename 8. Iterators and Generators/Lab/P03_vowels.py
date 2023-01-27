# Create a class called vowels, which should receive a string. Implement the __iter__ and __next__ methods,
# so the iterator returns only the vowels from the string.

class vowels:

    def __init__(self, string):
        self.string = string
        self.start = 0
        self.end = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start <= self.end:
            current = self.string[self.start]
            self.start += 1
            if current in "AEIOUaeiou":
                return current
        else:
            raise StopIteration()


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)




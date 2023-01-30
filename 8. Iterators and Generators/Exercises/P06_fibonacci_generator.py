# Create a generator function called fibonacci() that generates the Fibonacci numbers infinitely. The first two
# numbers in the sequence are always 0 and 1. Each following Fibonacci number is created by the sum of the current
# number with the previous one.


def fibonacci():
    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1

    while True:
        next_number = fib0 + fib1
        yield next_number
        fib0 = fib1
        fib1 = next_number


generator = fibonacci()
for i in range(5):
    print(next(generator))

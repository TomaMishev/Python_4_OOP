# Create a generator function called squares that should receive a number n. It should generate the squares of all
# numbers from 1 to n (inclusive).

def squares(n):
    counter = 1
    while counter <= n:
        yield counter * counter
        counter += 1



print(list(squares(5)))
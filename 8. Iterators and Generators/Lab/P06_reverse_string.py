# Create a generator function called reverse_text that receives a string and yields all string characters on one line
# in reversed order.


def reverse_text(string):
    counter = len(string) - 1
    while counter >= 0:
        yield string[counter]
        counter -= 1


for char in reverse_text("step"):
    print(char, end='')

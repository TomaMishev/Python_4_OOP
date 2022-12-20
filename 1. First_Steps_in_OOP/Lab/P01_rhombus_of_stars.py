# Create a program that reads a positive integer N as input and prints on the console a rhombus with size n:

def print_upper_part(num):
    for row in range(1, num + 1):
        for space in range(num - row):
            print(" ", end="")
        for star in range(1, row):
            print('*', end=" ")
        print("*")


def print_bottom_part(num):
    for row in range(num - 1, 0, -1):
        for space in range(num - row):
            print(" ", end="")
        for star in range(1, row):
            print('*', end=" ")
        print("*")


def print_rhombus(num):
    print_upper_part(num)
    print_bottom_part(num)


n = int(input())
print_rhombus(n)
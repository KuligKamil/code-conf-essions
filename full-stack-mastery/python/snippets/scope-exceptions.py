import os

import yaml


with open("data/data.yml") as f:
    data = yaml.load(f, Loader=yaml.FullLoader)
    print(data)
print(f)
print(data)
# data = yaml.load(f, Loader=yaml.FullLoader)  # run outside with statement ValueError: I/O operation on closed file.
print(data)
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError as e:
        print("Oops!  That was no valid number.  Try again...")

print(x, e)
import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lewat", "Paul McCartney", "George Harrison", "Ringo Star"]

## give a file name and it give u the extension back
def get_file_ext(filename):
    return filename[filename.index(".") + 1:]

## pass a num it will roll num pass of the dice
def roll_dice(num):
    return random.randint(1, num)
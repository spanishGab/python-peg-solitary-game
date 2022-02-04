from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'is_occupied'])
Square = namedtuple('Square', ['a', 'b', 'c', 'd'])

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

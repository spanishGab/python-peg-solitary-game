from collections import namedtuple

Point = namedtuple('Point', ['x', 'y', 'is_occupied'])
Square = namedtuple('Square', ['a', 'b', 'c', 'd'])
Color = namedtuple('Color', ['BOARD_COLOR',
                             'BOARD_BORDER',
                             'SQUARE_BORDER',
                             'AVALIABLE_MOVEMENT_BACKGROUND',
                             'AVALIABLE_MOVEMENT_BORDER'])

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3

BOARD_POSITION_FORMAT = '{vertical_position}:{horizontal_position}'

BACKGROUND_IMAGE = 'beech-red.jpg'
GAME_PIECE_IMAGE = 'game_piece.png'

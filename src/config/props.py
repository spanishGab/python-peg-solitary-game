from constants import Point, Color

SQUARE_EDGE = 70
BOARD_LENGTH = 7

BOARD = {
    '7:21': Point(x=195, y=55, is_occupied=True),
    '8:28': Point(x=265, y=55, is_occupied=True),
    '9:35': Point(x=335, y=55, is_occupied=True),
    '14:22': Point(x=195, y=125, is_occupied=True),
    '15:29': Point(x=265, y=125, is_occupied=True),
    '16:36': Point(x=335, y=125, is_occupied=True),
    '21:7': Point(x=55, y=195, is_occupied=True),
    '22:14': Point(x=125, y=195, is_occupied=True),
    '23:23': Point(x=195, y=195, is_occupied=True),
    '24:30': Point(x=265, y=195, is_occupied=True),
    '25:37': Point(x=335, y=195, is_occupied=True),
    '26:42': Point(x=405, y=195, is_occupied=True),
    '27:49': Point(x=475, y=195, is_occupied=True),
    '28:8': Point(x=55, y=265, is_occupied=True),
    '29:15': Point(x=125, y=265, is_occupied=True),
    '30:24': Point(x=195, y=265, is_occupied=True),
    '31:31': Point(x=265, y=265, is_occupied=False),
    '32:38': Point(x=335, y=265, is_occupied=True),
    '33:43': Point(x=405, y=265, is_occupied=True),
    '34:50': Point(x=475, y=265, is_occupied=True),
    '35:9': Point(x=55, y=335, is_occupied=True),
    '36:16': Point(x=125, y=335, is_occupied=True),
    '37:25': Point(x=195, y=335, is_occupied=True),
    '38:32': Point(x=265, y=335, is_occupied=True),
    '39:39': Point(x=335, y=335, is_occupied=True),
    '40:44': Point(x=405, y=335, is_occupied=True),
    '41:51': Point(x=475, y=335, is_occupied=True),
    '42:26': Point(x=195, y=405, is_occupied=True),
    '43:33': Point(x=265, y=405, is_occupied=True),
    '44:40': Point(x=335, y=405, is_occupied=True),
    '49:27': Point(x=195, y=475, is_occupied=True),
    '50:34': Point(x=265, y=475, is_occupied=True),
    '51:41': Point(x=335, y=475, is_occupied=True),
}


COLORS = Color(BOARD_COLOR=(77, 26, 0),
               BOARD_BORDER=(20, 20, 20),
               SQUARE_BORDER=(97, 51, 24),
               AVALIABLE_MOVEMENT_BACKGROUND=(153, 255, 102),
               AVALIABLE_MOVEMENT_BORDER=(102, 255, 26))

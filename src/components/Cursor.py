from config.constants import Square, UP, DOWN, LEFT, RIGHT
from config.props import BOARD, SQUARE_EDGE


class Cursor:

    def __init__(self,
                 x1: int = 195,
                 y1: int = 55,
                 x2: int = 265,
                 y2: int = 125):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

        self.shape = Square(
            a=(x1, y1),
            b=(x1, y2),
            c=(x2, y2),
            d=(x2, y1)
        )

    def move_cursor(self, pressed_key: bool, direction: int):
        if pressed_key:
            self.__make_movement(direction)

        self.__update_cursor()

    def check_movement_validity(self) -> bool:
        for name, point in BOARD.items():
            if self.x1 == point.x and self.y1 == point.y:
                return True

        return False

    def __make_movement(self, direction: int):
        if direction == UP:
            self.y1 -= SQUARE_EDGE
            self.y2 -= SQUARE_EDGE

            if not self.check_movement_validity():
                self.y1 += SQUARE_EDGE
                self.y2 += SQUARE_EDGE

        elif direction == DOWN:
            self.y1 += SQUARE_EDGE
            self.y2 += SQUARE_EDGE

            if not self.check_movement_validity():
                self.y1 -= SQUARE_EDGE
                self.y2 -= SQUARE_EDGE

        elif direction == LEFT:
            self.x1 -= SQUARE_EDGE
            self.x2 -= SQUARE_EDGE

            if not self.check_movement_validity():
                self.x1 += SQUARE_EDGE
                self.x2 += SQUARE_EDGE

        elif direction == RIGHT:
            self.x1 += SQUARE_EDGE
            self.x2 += SQUARE_EDGE

            if not self.check_movement_validity():
                self.x1 -= SQUARE_EDGE
                self.x2 -= SQUARE_EDGE

        def __update_cursor(self):
            self.shape.a = (self.x1, self.y1)
            self.shape.b = (self.x1, self.y2)
            self.shape.c = (self.x2, self.y2)
            self.shape.d = (self.x2, self.y1)

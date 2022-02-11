from config.constants import (
    UP, DOWN, LEFT, RIGHT, BOARD_POSITION_FORMAT, Square, Point
)
from config.props import SQUARE_EDGE, BOARD_LENGTH


class Cursor:

    def __init__(self,
                 position: str,
                 x1: int = 195,
                 y1: int = 55,
                 x2: int = 265,
                 y2: int = 125):
        self.position = position

        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2

        self.points = Square(
            a=Point(x=self._x1, y=self._y1),
            b=Point(x=self._x1, y=self._y2),
            c=Point(x=self._x2, y=self._y2),
            d=Point(x=self._x2, y=self._y1)
        )

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position: str):
        self.position = position.split(':')

    def move_cursor(self, pressed_key: bool, direction: int):
        if pressed_key:
            self.__make_movement(direction)

        self.__update_cursor()

    def is_vlaid_movement(self, direction: int) -> bool:
        is_vlaid_movement = False

        if direction == UP:
            is_vlaid_movement = (self.position[1] % BOARD_LENGTH) > 0
        if direction == DOWN:
            is_vlaid_movement = (self.position[1] % BOARD_LENGTH) not in (2, 6)
        if direction == LEFT:
            is_vlaid_movement = (self.position[0] % BOARD_LENGTH) > 0
        if direction == RIGHT:
            is_vlaid_movement = (self.position[0] % BOARD_LENGTH) not in (2, 6)

        return is_vlaid_movement

    def __make_movement(self, direction: int):
        if self.is_vlaid_movement(direction):
            if direction == UP:
                self.position = BOARD_POSITION_FORMAT.format(
                    vertical_position=self.position[0] - BOARD_LENGTH,
                    horizontal_position=self.position[1]
                )

            elif direction == DOWN:
                self._y1 += SQUARE_EDGE
                self._y2 += SQUARE_EDGE
                self.position = BOARD_POSITION_FORMAT.format(
                    vertical_position=self.position[0] + BOARD_LENGTH,
                    horizontal_position=self.position[1]
                )

            elif direction == LEFT:
                self._x1 -= SQUARE_EDGE
                self._x2 -= SQUARE_EDGE
                self.position = BOARD_POSITION_FORMAT.format(
                    vertical_position=self.position[0],
                    horizontal_position=self.position[1] - BOARD_LENGTH
                )

            elif direction == RIGHT:
                self._x1 += SQUARE_EDGE
                self._x2 += SQUARE_EDGE
                self.position = BOARD_POSITION_FORMAT.format(
                    vertical_position=self.position[0],
                    horizontal_position=self.position[1] + BOARD_LENGTH
                )

        def __update_cursor(self):
            self.position.a.x = self._x1
            self.position.a.y = self._y1

            self.position.b.x = self._x1
            self.position.b.y = self._y2

            self.position.c.x = self._x2
            self.position.c.y = self._y2

            self.position.d.x = self._x2
            self.position.d.y = self._y1

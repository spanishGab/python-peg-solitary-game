import pygame

from config.props import SQUARE_EDGE, Point
from Cursor import Cursor

MOVEMENT_SUM = SQUARE_EDGE * 2


class Piece:
    def __init__(self, piece_size: int = SQUARE_EDGE):
        self.green_square = pygame.Surface((piece_size, piece_size))

    def select_available_movements(self, cursor: Cursor, tab_positions: dict):
        self.green_square.fill((153, 255, 102))

        possible_movement_positions = (
            # MOVING UP
            (
                (Point(x=cursor.position.a.x, y=(cursor.position.a.y - MOVEMENT_SUM))),
                (Point(x=cursor.position.a.x, y=(cursor.position.a.y - SQUARE_EDGE)))
            ),
            # MOVING DOWN
            (
                (Point(x=cursor.position.a.x, y=(cursor.position.a.y + MOVEMENT_SUM))),
                (Point(x=cursor.position.a.x, y=(cursor.position.a.y + SQUARE_EDGE)))
            ),
            # MOVING LEFT
            (
                (Point(x=(cursor.position.a.x - MOVEMENT_SUM), y=cursor.position.a.y)),
                (Point(x=(cursor.position.a.x - SQUARE_EDGE), y=cursor.position.a.y))
            ),
            # MOVING RIGHT
            (
                (Point(x=(cursor.position.a.x + MOVEMENT_SUM), y=cursor.position.a.y)),
                (Point(x=(cursor.position.a.x + SQUARE_EDGE), y=cursor.position.a.y))
            ),
        )

        vacant_places = []
        for position in possible_movement_positions:
            for tab_position in tab_positions:
                if (position[0].x == tab_position.x and
                    position[0].y == tab_position.y):
                    if not tab_position.is_occupied and 
            if position[0] in list(tab_positions) and not tab_positions[position[0]] and tab_positions[position[1]]:
                vacant_places.append(position[0])

        # vacant_places = [v[0] for v in list(sum_types.values()) if v[0] in list(tab_positions) and not tab_positions[v[0]] and tab_positions[v[1]]]

        if to_paint:
            for i in to_paint:
                if not tab_positions[i]:  # plot a green square in the available position(s)
                    screen.blit(green_square, i)
                    pygame.draw.lines(screen, (102, 255, 26), True, [(i[0], i[1]), (i[0], i[1]+70), (i[0]+70, i[1]+70), (i[0]+70, i[1])], 3)
        
        return to_paint
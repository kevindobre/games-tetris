import pygame as pg

vec = pg.math.Vector2

FPS = 60
FIELD_COLOR = (48, 39, 32)
BG_COLOR = (24, 89, 117)

FONT_PATH = 'FREAKSOFNATUREMASSIVE.ttf'

ANIM_TIME_INTERVAL = 150  # milliseconds
FAST_ANIM_TIME_INTERVAL = 15

TITLE_SIZE = 50
FIELD_SIZE = FIELD_WIDTH, FIELD_HEIGHT = 10, 14
FIELD_RES = FIELD_WIDTH * TITLE_SIZE, FIELD_HEIGHT * TITLE_SIZE

FIELD_SCALE_W, FIELD_SCALE_H = 1.7, 1.0
WIN_RES = WIN_WIDTH, WIN_HEIGHT = FIELD_RES[0] * FIELD_SCALE_W, FIELD_RES[1] * FIELD_SCALE_H

INIT_POS_OFFSET = vec(FIELD_WIDTH // 2 - 1, 0)
NEXT_POS_OFFSET = vec(FIELD_WIDTH * 1.3, FIELD_HEIGHT * 0.45)
MOVE_DIRECTIONS = {'LEFT': vec(-1, 0), 'RIGHT': vec(1, 0), 'DOWN': vec(0, 1)}

TETROMINOES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}
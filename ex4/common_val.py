# -------------------------------------------------------------------------------------
#   Imports:
# -------------------------------------------------------------------------------------
import pygame

# -------------------------------------------------------------------------------------
#   Colors properties:
# -------------------------------------------------------------------------------------
WHITE = (199, 231, 207)
BLACK = (51, 55, 69)
RED = (230, 52, 98)
BEIGE = (238, 245, 219)

# -------------------------------------------------------------------------------------
#   Board properties:
# -------------------------------------------------------------------------------------
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
ROWS = 8
COLS = 8
SQUARE_SIZE = int(WINDOW_WIDTH / COLS)

# -------------------------------------------------------------------------------------
#   King disc properties:
# -------------------------------------------------------------------------------------
pygame.font.init()
KING = pygame.font.SysFont('ubuntu', 80).render('K', False, RED)

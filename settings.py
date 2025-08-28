WIDTH, HEIGHT = 1280, 720
FPS = 60
TITLE = "Bisk"

# Colors
BG = (20, 20, 26)
FG = (235, 235, 240)
ACCENT = (239, 176, 52)
TEXT = (235, 235, 240)
BTN = (40, 40, 50)
BTN_HOVER = (60, 60, 78)
BTN_WIDTH = 280
BTN_HEIGHT = 64

START_MENU_BUTTON_TOP_OFFSET = 24
START_MENU_BUTTON_SPACING = 16
START_MENU_TAG_OFFSET = 64

TITLE_FONT_SIZE = 96
BODY_FONT_SIZE = 28
BUTTON_FONT_SIZE = 40

# Board
BOARD_PADDING = 10  # pixels between edge of screen and board
BOARD_X_DIM = 5  # Number of cells on x-axis
BOARD_Y_DIM = 4  # Number of cells on y-axis

# Regions
REGION_COUNT = 5

# Territories
TERRITORY_COUNT = 20

assert TERRITORY_COUNT <= BOARD_X_DIM * BOARD_Y_DIM  # Need enough board space

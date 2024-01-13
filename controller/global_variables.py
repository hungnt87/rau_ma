import pydirectinput

from controller import ConfigManager, Event, PathManager, SelectWindow
from controller.filelog import logger

config = ConfigManager("config.ini")
config.create_config({"AutoConfig": {"burn": "10", "move": "False", "like": "False"}})
character_moves_event = Event("character_moves_event")
global_event = Event("global_event")
path = PathManager()

count_of_buy = 0
money = True

# window_x, window_y, window_width, window_height =
CONFIDENCE = 0.8
GRAYSCALE = True
REGION = (0, 0, 1920, 1080)
window_x = 0
window_y = 0
window_height = 1920
window_width = 1080


def bot_initialization():
    global CONFIDENCE, GRAYSCALE, REGION, window_x, window_y, window_width, window_height
    dota2 = SelectWindow("Dota 2")
    if dota2.hwnd is None:
        # logger.debug("Không tìm thấy cửa sổ có tiêu đề 'Dota 2'")
        return None
    else:
        window_x, window_y, window_width, window_height = dota2.get_window_region()
        REGION = (window_x, window_y, window_width, window_height)
    pydirectinput.FAILSAFE = False
    pydirectinput.PAUSE = 0.05

    # logger.debug("Initialization completed.")


def check_money():
    global money
    return money


def set_money(status):
    global money
    money = status


def get_count_of_buy():
    global count_of_buy
    return count_of_buy


def add_count_of_buy(number):
    global count_of_buy
    count_of_buy += number


def reset_count_of_buy():
    global count_of_buy
    count_of_buy = 0


if __name__ == "__main__":
    pass

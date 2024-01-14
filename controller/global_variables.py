import pydirectinput

from controller import ConfigManager, Event, PathManager, Region_Window, SelectWindow
from controller.filelog import logger

config = ConfigManager("config.ini")
config.create_config({"AutoConfig": {"burn": "10", "move": "False", "like": "False"}})
character_moves_event = Event("character_moves_event")
global_event = Event("global_event")
path = PathManager()

count_of_buy = 0
money = True

REGION = Region_Window("Dota 2")
region_hero = Region_Window("hero")
region_sell_hero = Region_Window("sell_hero")
region_item = Region_Window("item")


def bot_initialization():
    global REGION, region_hero, region_sell_hero, region_item
    dota2 = SelectWindow("Dota 2")
    if dota2.hwnd is None:
        # logger.debug("Không tìm thấy cửa sổ có tiêu đề 'Dota 2'")
        return None
    else:
        REGION.x, REGION.y, REGION.width, REGION.height = dota2.get_window_region()

        region_hero.x = REGION.x + 537
        region_hero.y = REGION.y + 125
        region_hero.width = 1158
        region_hero.height = 406

        region_sell_hero.x = REGION.x + 662
        region_sell_hero.y = REGION.y + 791
        region_sell_hero.width = 704
        region_sell_hero.height = 358

        region_item.x = REGION.x + 394
        region_item.y = REGION.y + 321
        region_item.width = 1384
        region_item.height = 692

    pydirectinput.FAILSAFE = False
    pydirectinput.PAUSE = 0.1

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

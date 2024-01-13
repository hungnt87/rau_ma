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


def bot_initialization():
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

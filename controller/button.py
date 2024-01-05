import os
import sys
import threading
import pyautogui
import time
from log import logger
import pydirectinput
from global_variables import Global_variables as gv

from log import logger

gv = gv()


class Button:
    def __init__(self):
        self.name = para_name


if __name__ == "__main__":
    logger.info("Start")
    path = os.path.join("data", "imgae", "item")
    path = gv.resource_path(path)
    logger.info(path)
    i = -0
    while True:        
        if gv.check_event():
            break
        i += 1
        logger.info(i)
        time.sleep(1)
        if

    pass

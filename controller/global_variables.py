import os
import sys
import threading
import pyautogui
import time
from log import logger

event_stop = threading.Event()
event_pause = threading.Event()


class Global_variables:
    def __init__(self):
        self.name = "Global_variables"

    def app_start(self):
        event_pause.set()
        event_stop.clear()

    def app_stop(self):
        event_stop.set()
        event_pause.set()

    def app_pause(self):
        if event_pause.is_set():
            event_pause.clear()
            logger.debug("App paused")
        else:
            event_pause.set()
            logger.debug("App resumed")

    def app_resume(self):
        event_pause.set()
        logger.debug("App resumed")

    def check_event(self):
        if event_stop.is_set():
            return True
        event_pause.wait()
        return False


gv = Global_variables()


def check_event(func):
    def wrapper():
        if gv.check_event():
            return
        func()

    return wrapper


def resource_path(relative_path):
    """Get absolute path to resource, works for dev and for PyInstaller"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


if __name__ == "__main__":
    pass

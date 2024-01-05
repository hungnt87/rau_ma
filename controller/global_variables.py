import os
import sys
import threading
import pyautogui
import time
from log import logger


class Global_variables:
    def __init__(self):
        self.event_stop = threading.Event()
        self.event_pause = threading.Event()
        self.event_pause.set()

    def check_event(self):
        if self.event_stop.is_set():
            return True
        else:
            return False
        self.event_pause.wait()

    @staticmethod
    def resource_path(relative_path):
        """Get absolute path to resource, works for dev and for PyInstaller"""
        try:
            # PyInstaller creates a temp folder and stores path in _MEIPASS
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.abspath(".")

        return os.path.join(base_path, relative_path)

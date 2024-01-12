import configparser
import threading
import time

import pydirectinput
import PySimpleGUI as sg

from controller.filelog import OutputHandler, logger
from controller.global_variables import Dota2, character_moves_event, global_event, path
from interface import main_window

if __name__ == "__main__":
    # window_config_auto()
    main_window()
    pass

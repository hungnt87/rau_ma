import configparser
import os
import sys
import threading
import time

import pyautogui
import pydirectinput
import win32api
import win32con
import win32gui

from controller.filelog import logger

# from controller.global_variables import global_event


class ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config = configparser.ConfigParser()

    def check_config_exists(self):
        return os.path.exists(self.config_file)

    def create_config(self, default_config={}):
        if not self.check_config_exists():
            logger.debug(
                f"Config file ({self.config_file}) not found. Creating a new one..."
            )

            # Set default configuration
            self.config.read_dict(default_config)

            # Save the configuration to the file
            with open(self.config_file, "w") as config_file:
                self.config.write(config_file)

            logger.debug(f"New config file created: {self.config_file}")

    def read_config(self, section, key):
        if self.check_config_exists():
            # logger.debug(f"Found config file ({self.config_file}). Reading...")

            # Read configuration from the file
            self.config.read(self.config_file)

            # Get the configuration
            return self.config[section][key]
        else:
            print(f"Config file not found: {self.config_file}")

    def save_config(self, section, key, value):
        if self.check_config_exists():
            # logger.debug(f"Found config file ({self.config_file}). Reading...")

            # Read configuration from the file
            self.config.read(self.config_file)

            # Get the configuration
            self.config[section][key] = value
            with open(self.config_file, "w") as config_file:
                self.config.write(config_file)
        else:
            print(f"Config file not found: {self.config_file}")


class Event:
    def __init__(self, para_name):
        self.name = para_name
        self.event_stop = threading.Event()
        self.event_pause = threading.Event()
        self.event_pause.set()
        self.event_stop.clear()

    def app_start(self):
        self.event_pause.set()
        self.event_stop.clear()
        logger.debug(f"{self.name} started")

    def app_stop(self):
        self.event_pause.set()
        self.event_stop.set()
        logger.debug(f"{self.name} stopped")

    def app_pause(self):
        self.event_pause.clear()

    def app_resume(self):
        self.event_pause.set()

    def check_event(self):
        if self.event_stop.is_set():
            return True
        self.event_pause.wait()
        return False

    def sleep(self, time_sleep=1):
        i = 0
        while True:
            if self.check_event():
                return False
            i += 0.1
            if i > time_sleep:
                break
            time.sleep(0.1)


class PathManager:
    base_path = ""

    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def get_absolute_path(self, relative_path):
        # Kết hợp đường dẫn cơ sở và đường dẫn tương đối để có đường dẫn tuyệt đối
        return os.path.join(self.base_path, relative_path)

    @staticmethod
    def get_resource_path(relative_path):
        # If the script is frozen (e.g., PyInstaller), use sys._MEIPASS
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            # If the script is not frozen, use the directory of the script
            base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        # Combine the base path and the relative path to get the absolute path
        absolute_path = os.path.join(base_path, relative_path)
        return absolute_path


class SelectWindow:
    hwnd = None

    def __init__(self, app_name):
        self.app_name = app_name
        self.hwnd = self.get_app_window_handle()

    def get_app_window_handle(self):
        hwnd = win32gui.FindWindow(None, self.app_name)
        if hwnd:
            self.hwnd = hwnd
            return hwnd
        else:
            # logger.debug(f"Không tìm thấy cửa sổ có tiêu đề '{self.app_name}'")
            return None

    def set_foreground(self):
        win32gui.SetForegroundWindow(self.hwnd)

    def move_window_to(self, x=0, y=0):
        # Lấy kích thước hiện tại của cửa sổ
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)

        # Thay đổi kích thước và vị trí của cửa sổ
        win32gui.SetForegroundWindow(self.hwnd)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOP, x, y, width, height, 0)

    def get_region(self):
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)
        return 0, 0, width, height

    def get_window_position(self):
        x, y, width, height = win32gui.GetWindowRect(self.hwnd)
        return x, y

    def get_window_region(self):
        x, y, width, height = win32gui.GetWindowRect(self.hwnd)
        return x, y, width, height

    def get_window_info(self):
        try:
            # Lấy danh sách các cửa sổ với tiêu đề tương ứng
            windows = pyautogui.getWindowsWithTitle(self.app_name)

            # Lấy thông tin về cửa sổ đầu tiên trong danh sách
            target_window = windows[0]
            window_position = (target_window.left, target_window.top)
            window_size = (target_window.width, target_window.height)

            print(f"Thông tin cửa sổ '{self.app_name}':")
            print(f"  Vị trí: {window_position}")
            print(f"  Kích thước: {window_size}")
            center_x = (window_size[0] // 2) + window_position[0]
            center_y = (window_size[1] // 2) + window_position[1]
            pydirectinput.moveTo(center_x, center_y)
            print(f"  Tọa độ trung tâm: ({center_x}, {center_y})")
            return window_position, window_size

        except Exception as e:
            print(f"Lỗi: {e}")
            return None

    def get_center_window(self):
        try:
            # Lấy danh sách các cửa sổ với tiêu đề tương ứng
            windows = pyautogui.getWindowsWithTitle(self.app_name)
            # Lấy thông tin về cửa sổ đầu tiên trong danh sách
            target_window = windows[0]
            window_position = (target_window.left, target_window.top)
            window_size = (target_window.width, target_window.height)

            center_x = (window_size[0] // 2) + window_position[0]
            center_y = (window_size[1] // 2) + window_position[1]
            # logger.debug(f"  Tọa độ trung tâm: ({center_x}, {center_y})")
            return center_x, center_y

        except Exception as e:
            print(f"Lỗi: {e}")
            return None


class Region_Window:
    def __init__(self, name):
        self.name = name
        self.x = 0
        self.y = 0
        self.width = 1920
        self.height = 1080


if __name__ == "__main__":
    # dota2 = SelectWindow("Dota 2")
    # # dota2.move_window_to(0, 0)
    # dota2.set_foreground()
    # # dota2.get_center_window()
    # x, y = dota2.get_window_position()
    # logger.debug(f"X: {x}, Y: {y}")
    # print(PathManager.get_resource_path("config.ini"))
    pass

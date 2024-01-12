import configparser
import os
import threading

import win32api
import win32gui

from controller.filelog import logger

# from controller.global_variables import path


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
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Combine the base path and the relative path to get the absolute path
        absolute_path = os.path.join(base_path, relative_path)

        return absolute_path


class SelectWindow:
    hwnd = None

    def __init__(self, app_name):
        self.app_name = app_name
        self.hwnd = self.get_app_window_handle()

    def get_app_window_handle(self):
        if self.hwnd is None:
            self.hwnd = win32gui.FindWindow(None, self.app_name)
        return self.hwnd

    def move_window_to(self, x=0, y=0):
        # Lấy kích thước hiện tại của cửa sổ
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)

        # Thay đổi kích thước và vị trí của cửa sổ
        win32gui.SetForegroundWindow(self.hwnd)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOP, x, y, width, height, 0)

    def get_region(self):
        if global_event.check_event():
            return False
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)
        return 0, 0, width, height


if __name__ == "__main__":
    pass

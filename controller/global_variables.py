import os
import sys
import threading
import win32gui
import win32con
import controller.filelog as filelog

event_stop = threading.Event()
event_pause = threading.Event()
event_stop_exit_round = threading.Event()
event_pause_exit_round = threading.Event()
event_pause.set()
logger = filelog.logger


class Global_variables:
    name = ""
    money = None
    number_of_buy = None
    count_of_buy = None

    def __init__(self):
        self.name = "Global_variables"
        self.money = True
        self.number_of_buy = 0
        self.count_of_buy = 0

    def app_start(self):
        event_pause.set()
        event_stop.clear()
        logger.debug("App started")

    def app_stop(self):
        event_stop.set()
        event_pause.set()
        logger.debug("App stopped")

    def app_pause(self):
        if event_pause.is_set():
            event_pause.clear()
            logger.debug("App paused")
        else:
            event_pause.set()
            logger.debug("App resumed")

    def app_resume(self):
        event_pause.set()
        # logger.debug("App resumed")

    def check_event(self):
        if event_stop.is_set():
            return True
        event_pause.wait()
        return False

    def check_money(self):
        return self.money

    def set_money(self, money):
        self.money = money

    def get_number_of_buy(self):
        return self.number_of_buy

    def set_number_of_buy(self, number_of_buy):
        self.number_of_buy = number_of_buy

    def add_number_of_buy(self):
        self.number_of_buy += 1


class Event:
    event_stop = threading.Event()
    event_pause = threading.Event()
    event_stop_exit_round = threading.Event()
    event_pause_exit_round = threading.Event()

    def __init__(self):
        self.name = "event"
        self.event_stop.clear()
        self.event_pause.set()
        self.event_stop_exit_round.clear()

    def app_start(self):
        self.event_pause.set()
        self.event_stop.clear()
        logger.debug("App started")

    def app_stop(self):
        self.event_stop.set()
        self.event_pause.set()
        logger.debug("App stopped")

    def app_pause(self):
        if self.event_pause.is_set():
            self.event_pause.clear()
            logger.debug("App paused")
        else:
            self.event_pause.set()
            logger.debug("App resumed")

    def check_event(self):
        if self.event_stop.is_set():
            return True
        self.event_pause.wait()
        return False

    def set_event_stop_exit_round(self):
        self.event_stop_exit_round.set()

    def clear_event_stop_exit_round(self):
        self.event_stop_exit_round.clear()

    def set_pause_button_character_moves(self):
        self.event_pause_exit_round.clear()

    def set_resume_button_character_moves(self):
        self.event_pause_exit_round.set()

    def check_event_exit_round(self):
        if self.event_stop_exit_round.is_set():
            return True
        self.event_pause_exit_round.wait()
        return False


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
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            # If the script is not frozen, use the directory of the script
            base_path = os.path.dirname(os.path.abspath(__file__))

        # Combine the base path and the relative path to get the absolute path
        absolute_path = os.path.join(base_path, relative_path)

        return absolute_path


def get_app_window_handle(app_name):
    return win32gui.FindWindow(None, app_name)


class SelectWindow:
    hwnd = None

    def __init__(self, app_name):
        self.hwnd = get_app_window_handle(app_name)

    def move_window_to(self, x=0, y=0):
        # Lấy kích thước hiện tại của cửa sổ
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)

        # Thay đổi kích thước và vị trí của cửa sổ
        win32gui.SetForegroundWindow(self.hwnd)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOP, x, y, width, height, 0)

    def get_region(self):
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)
        return (0, 0, width, height)


def check_event(func):
    def wrapper():
        if gv.check_event():
            return
        func()

    return wrapper


gv = Global_variables()
path = PathManager()
if __name__ == "__main__":
    gv.add_number_of_buy()
    gv.add_number_of_buy()
    print(gv.get_number_of_buy())

    pass

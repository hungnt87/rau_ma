import os
import sys
import threading
import win32gui
import win32con
import controller.filelog as filelog
import time

logger = filelog.logger
# number_of_buy = None
count_of_buy = 0
money = True


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
        if self.event_pause.is_set():
            self.event_pause.clear()
            logger.debug(f"{self.name} paused")
        else:
            self.event_pause.set()
            logger.debug(f"{self.name} resumed")
    
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
        if getattr(sys, 'frozen', False):
            base_path = sys._MEIPASS
        else:
            # If the script is not frozen, use the directory of the script
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Combine the base path and the relative path to get the absolute path
        absolute_path = os.path.join(base_path, relative_path)
        
        return absolute_path


def get_app_window_handle(app_name):
    hwnd = None
    hwnd = win32gui.FindWindow(None, app_name)
    
    hWndex = win32gui.FindWindowEx(hwnd, None, None, None)
    logger.debug("hwnd: {}".format(hwnd))
    logger.debug("hWndex: {}".format(hWndex))
    return win32gui.FindWindow(None, app_name)


class SelectWindow:
    hwnd = None
    
    def __init__(self, app_name):
        self.hwnd = self.get_app_window_handle(app_name)
    
    def get_app_window_handle(self, app_name):
        hwnd = win32gui.FindWindow(None, app_name)
        
        return hwnd
    
    def move_window_to(self, x=0, y=0):
        # Lấy kích thước hiện tại của cửa sổ
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)
        
        # Thay đổi kích thước và vị trí của cửa sổ
        win32gui.SetForegroundWindow(self.hwnd)
        win32gui.SetWindowPos(self.hwnd, win32con.HWND_TOP, x, y, width, height, 0)
    
    def get_region(self):
        _, _, width, height = win32gui.GetWindowRect(self.hwnd)
        return (0, 0, width, height)


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


path = PathManager()

global_event: Event = Event("global_event")
character_moves_event = Event("character_moves_event")
if __name__ == "__main__":
    get_app_window_handle("03. Danh mục Hồ sơ thanh toán.docx  -  AutoRecovered  -  Compatibility Mode - Word")
    pass

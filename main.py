import round as r
import win32gui
import win32con
import time
import button
from datetime import datetime
#import logging
from log import logger


#logging.basicConfig(level=logging.DEBUG, filename="log.txt", format = ('%(asctime)s - %(levelname)s - %(message)s'))

app_name = "Dota 2"
new_x, new_y = -1, 0  # Tọa độ mới bạn muốn di chuyển cửa sổ đến


def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd


def move_window_to(handle, x, y):
    # Lấy kích thước hiện tại của cửa sổ
    _, _, width, height = win32gui.GetWindowRect(handle)

    # Thay đổi kích thước và vị trí của cửa sổ
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, x, y, width, height, 0)


hwnd = get_app_window_handle(app_name)

if hwnd:
    time.sleep(1)
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(1)
    move_window_to(hwnd, new_x, new_y)
    #print(f"Tim thay cua so  '{app_name}'")
    logger.info(f"Tim thay cua so  '{app_name}'")

    for n in range(0, 20):
       #print("Date {} Bat dau auto lan: {}".format(datetime.now().time(),n))
        logger.info("Date {} Bat dau auto lan: {}".format(datetime.now().time(),n))
        r.round_all(n)
        button.exit_game_round20()
        #print("Date {}  :Ket thuc auto lan {}".format(datetime.now().time(),n))
        logger.info("Date {}  :Ket thuc auto lan {}".format(datetime.now().time(),n))
        time.sleep(20)
    

else:
    #print(f"Không tìm thấy cửa sổ có tên '{app_name}'")
    
    logger.info("Khong tim thay cua so co ten {}".format(app_name))
    
    #logger.info("Khong tim thay cua so co ten {}".format(app_name))
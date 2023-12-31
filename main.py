import round as r
import win32gui
import win32con
import time
import button
from datetime import datetime

# import logging
from log import logger


def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd


def move_window_to(handle, x, y):
    # Lấy kích thước hiện tại của cửa sổ
    _, _, width, height = win32gui.GetWindowRect(handle)

    # Thay đổi kích thước và vị trí của cửa sổ
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, x, y, width, height, 0)


def main():
    # ten cua so
    app_name = "Dota 2"
    # toa do cua so
    new_x, new_y = 0, 0
    hwnd = get_app_window_handle(app_name)

    if hwnd:
        time.sleep(1)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
        move_window_to(hwnd, new_x, new_y)
        # print(f"Tim thay cua so  '{app_name}'")
        logger.info(f"Tim thay cua so  '{app_name}'")

        for n in range(0, 20):
            # print("t dau auto lan: {}".format(n))
            logger.info("Bat dau auto lan: {}".format(n))
            r.round_all(n)
            button.exit_game_round20()
            # print("Ket thuc auto lan {}".format(n))
            logger.info("Ket thuc auto lan {}".format(n))
            for t in range(20):
                t = 20 - t
                # print("Dang cho 5s")
                logger.info(f"Dang cho bat auto lai sau {t}/20s")
                time.sleep(1)

    else:
        logger.info("Khong tim thay cua so co ten {}".format(app_name))


if __name__ == "__main__":
    main()

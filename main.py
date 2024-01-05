import PySimpleGUI as sg
import threading
import win32gui
import win32con
import time
import button
import logging
import queue
from log import logger
import round as r
import keyboard
import controller.global_variables as cgv


gv = cgv.Global_variables()


def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd


def move_window_to(handle, x, y):
    # Lấy kích thước hiện tại của cửa sổ
    _, _, width, height = win32gui.GetWindowRect(handle)

    # Thay đổi kích thước và vị trí của cửa sổ
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, x, y, width, height, 0)


main_status = False


def main():
    global main_status, gv
    # ten cua so
    app_name = "Dota 2"
    # toa do cua so
    new_x, new_y = 0, 0
    hwnd = get_app_window_handle(app_name)
    n = 0
    if hwnd:
        time.sleep(1)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
        move_window_to(hwnd, new_x, new_y)
        # print(f"Tim thay cua so  '{app_name}'")
        logger.info(f"Tim thay cua so  '{app_name}'")
        main_status = True
        while True:
            if gv.check_event():
                # logger.info("Stop thread main")
                break
            n += 1
            # print("t dau auto lan: {}".format(n))
            logger.info("Bat dau auto lan: {}".format(n))
            if r.round_all(n) is False:
                break
            if button.exit_game_round20() is False:
                break
            logger.info("Ket thuc auto lan {}".format(n))
            for t in range(10):
                if gv.check_event():
                    break

                t = 10 - t
                # print("Dang cho 5s")
                logger.info(f"Dang cho bat auto lai sau {t}/10s")
                time.sleep(1)

        else:
            main_status = False
            logger.info("Khong tim thay cua so co ten {}".format(app_name))


class ThreadedApp:
    global main_status

    def __init__(self):
        self.t1 = threading.Thread()

    def run(self):
        gv.app_start()
        self.t1 = threading.Thread(target=main, args=(), daemon=True)
        self.t1.start()

    def stop(self):
        gv.app_stop()

    def pause(self):
        gv.app_pause()
        # self._pause_event.set()

    def resume(self):
        gv.app_resume()
        # self._pause_event.clear()


class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)


# pause = threading.Event()


def gui():
    global main_status
    button_pause = "Pause (Ctrl + F11)"
    layout = [
        [
            sg.Button("Start (Ctrl + F9)", bind_return_key=True, key="-START-"),
            sg.Button("Stop (Ctrl + F10)", key="-STOP-", disabled=True),
            sg.Button(button_pause, key="-PAUSE-", disabled=True),
        ],
        [sg.Output(size=(60, 10), key="-LOG-")],
        [sg.Button("Exit")],
    ]
    # format_log = logging.Formatter("[%(asctime)s] - [%(levelname)s] - %(message)s")
    window = sg.Window(
        "Brodota-bot",
        layout,
        default_element_size=(30, 2),
        font=("Helvetica", " 10"),
        default_button_element_size=(8, 2),
        # background_color="red",
        keep_on_top=True,
        # transparent_color="red",
        alpha_channel=1,
        grab_anywhere=True,
    )

    appStarted = False
    log_queue = queue.Queue()
    queue_handler = QueueHandler(log_queue)
    logger.addHandler(queue_handler)
    threadedApp = ThreadedApp()

    while True:
        event, values = window.read(timeout=100)
        if main_status:
            window["-START-"].update(disabled=True)
            window["-STOP-"].update(disabled=False)
            window["-PAUSE-"].update(disabled=False)
        else:
            window["-START-"].update(disabled=False)
            window["-STOP-"].update(disabled=True)
            window["-PAUSE-"].update(disabled=True)
        if event == "-START-":
            if appStarted is False:
                threadedApp.run()
                logger.debug("App started")
                appStarted = True
        elif event in (sg.WIN_CLOSED, "Exit"):
            if threadedApp:
                threadedApp.stop()
            break
        elif event == "-STOP-":
            if threadedApp:
                threadedApp.stop()
                # threadedApp.join()
                logger.debug("App stopped")
                window["-START-"].update(disabled=False)
                window["-PAUSE-"].update(disabled=True)
                window["-STOP-"].update(disabled=True)
                appStarted = False
                main_status = False
        elif event == "-PAUSE-":
            # pause.set()
            # button_pause = "Resume"
            if threadedApp:
                threadedApp.pause()
                if button_pause == "Pause":
                    button_pause = "Resume (Ctrl + F11)"
                else:
                    button_pause = "Pause (Ctrl + F11)"
            #     # button_pause = "Resume"
            window["-PAUSE-"].update(button_pause)
            # window["-S-"].update(disabled=True)

        try:
            record = log_queue.get(block=False)
        except queue.Empty:
            pass
        else:
            msg = queue_handler.format(record)
            window["-LOG-"].update(msg + "\n", append=True)

    window.close()


def test1():
    i = 0
    while True:
        i += 1
        print(f"test1 {i}")
        time.sleep(1)
        if i == 5:
            break


def test2():
    i = 0
    while True:
        if gv.check_event():
            break
        i += 1
        print(f"test2 {i}")
        time.sleep(1)
        if i == 5:
            break


def main1():
    global main_status
    main_status = True
    test1()
    test2()


if __name__ == "__main__":
    # main(pause_event=event_pause, stop_event=event_stop)
    gui()

    pass

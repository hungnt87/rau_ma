import PySimpleGUI as sg
import threading
import win32gui
import win32con
import time
import button
import logging
import queue
from log import logger

import keyboard
import round as r

event_stop = threading.Event()
event_pause = threading.Event()
main_status = False
# Setup logging and start app


def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd


def move_window_to(handle, x, y):
    # Lấy kích thước hiện tại của cửa sổ
    _, _, width, height = win32gui.GetWindowRect(handle)

    # Thay đổi kích thước và vị trí của cửa sổ
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, x, y, width, height, 0)


def main(stop_event=event_stop, pause_event=event_pause):
    # global main_status
    # main_status = True
    # r.round_all(round_number=1, stop_event=stop_event, pause_event=pause_event)
    global main_status
    # ten cua so
    app_name = "Dota 2"
    # toa do cua so
    new_x, new_y = 0, 0
    hwnd = get_app_window_handle(app_name)

    if hwnd:
        main_status = True
        time.sleep(1)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
        move_window_to(hwnd, new_x, new_y)
        # print(f"Tim thay cua so  '{app_name}'")
        logger.info(f"Tim thay cua so  '{app_name}'")
        n = 0
        while True:
            if stop_event.is_set():
                logger.info("Stop thread main")
                break
            pause_event.wait()
            n += 1
            # print("t dau auto lan: {}".format(n))
            logger.info("Bat dau auto lan: {}".format(n))
            r.round_all(n, stop_event=stop_event, pause_event=pause_event)
            button.exit_game_round20()
            # print("Ket thuc auto lan {}".format(n))
            logger.info("Ket thuc auto lan {}".format(n))
            for t in range(20):
                if stop_event.is_set():
                    logger.info("Stop thread main")
                    break
                pause_event.wait()
                t = 20 - t
                # print("Dang cho 5s")
                logger.info(f"Dang cho bat auto lai sau {t}/20s")
                time.sleep(1)

    else:
        main_status = False
        logger.info("Khong tim thay cua so co ten {}".format(app_name))


class ThreadedApp:
    def __init__(self):
        self._stop_event = threading.Event()
        self._pause_event = threading.Event()
        self.t1 = threading.Thread()

    def run(self):
        # r.round_all(round_number=1, stop_event=self._stop_event)
        self._pause_event.set()
        self._stop_event.clear()
        r.set_event_run()
        self.t1 = threading.Thread(
            target=main, args=(self._stop_event, self._pause_event), daemon=True
        )
        self.t1.start()

    def stop(self):
        # self._pause_event.set()
        self._stop_event.set()
        self._pause_event.set()
        r.set_event_stop()
        # self.t1._stop()
        self.t1.join()

    def pause(self):
        if self._pause_event.is_set():
            self._pause_event.clear()
            r.set_event_pause()
            logger.debug("App paused")
        else:
            self._pause_event.set()
            r.set_event_resume()
            logger.debug("App resumed")
        # self._pause_event.clear()

    def t1_is_alive(self):
        return self.t1.is_alive()


class QueueHandler(logging.Handler):
    def __init__(self, log_queue):
        super().__init__()
        self.log_queue = log_queue

    def emit(self, record):
        self.log_queue.put(record)


def gui():
    global event_stop, event_pause, threadedApp, main_status
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
        if event == "-START-":
            if appStarted is False:
                threadedApp.run()
                logger.debug("App started")
                if main_status:
                    window["-START-"].update(disabled=True)
                    window["-STOP-"].update(disabled=False)
                    window["-PAUSE-"].update(disabled=False)
                    appStarted = True
        elif event in (sg.WIN_CLOSED, "Exit"):
            # event_stop.set()
            if threadedApp:
                threadedApp.stop()
                # threadedApp.join()
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
        elif event == "-PAUSE-":
            if threadedApp:
                threadedApp.pause()
                if button_pause == "Pause":
                    button_pause = "Resume (Ctrl + F11)"
                else:
                    button_pause = "Pause (Ctrl + F11)"
                # button_pause = "Resume"
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


if __name__ == "__main__":
    gui()
    # t1.join()

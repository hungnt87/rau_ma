import PySimpleGUI as sg
import win32gui
import win32con
import time
import button
from datetime import datetime
import logging
from log import logger
import tkinter as tk  # Python 3.x
import tkinter.scrolledtext as ScrolledText
import threading
import keyboard
import round as r

event_main = threading.Event()


class TextHandler(logging.Handler):
    # This class allows you to log to a Tkinter Text or ScrolledText widget
    # Adapted from Moshe Kaplan: https://gist.github.com/moshekaplan/c425f861de7bbf28ef06
    format_log = "%(asctime)s\t %(levelname)s\t %(message)s"

    file_logger_format = logging.Formatter(format_log)

    def __init__(self, text):
        # run the regular Handler __init__
        logging.Handler.__init__(self)
        # Store a reference to the Text it will log to
        self.text = text

    def emit(self, record):
        msg = self.format(record)

        def append():
            self.text.configure(state="normal")
            self.text.insert(tk.END, msg + "\n")
            self.text.configure(state="disabled")
            # Autoscroll to the bottom
            self.text.yview(tk.END)

        # This is necessary because we can't modify the Text from other threads
        self.text.after(0, append)


class myGUI(tk.Frame):
    # This class defines the graphical user interface

    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.root = parent
        self.build_gui()

    def build_gui(self):
        # Build GUI
        global IsOpen
        self.root.title("Brodota-bot")
        self.root.option_add("*tearOff", "FALSE")
        self.grid(column=0, row=3, sticky="ew")
        self.grid_columnconfigure(0, weight=1, uniform="a")
        self.grid_columnconfigure(1, weight=1, uniform="a")
        self.grid_columnconfigure(2, weight=1, uniform="a")
        self.grid_columnconfigure(3, weight=1, uniform="a")
        button1 = tk.Button(self, text="Start (Ctrl+F10)", command=threading_main)
        button1.grid(column=0, row=0, sticky="ew")
        button2 = tk.Button(self, text="Stop (Ctrt + F11)", command=threading_test)
        button2.grid(column=1, row=0, sticky="ew")
        # butt
        # Add text widget to display logging info
        st = ScrolledText.ScrolledText(self, state="disabled")
        st.grid(column=0, row=1, sticky="w", columnspan=4)
        st.configure(font="TkFixedFont")
        st.grid(column=0, row=1, sticky="w", columnspan=4)
        format_log = logging.Formatter("[%(asctime)s] - [%(levelname)s] - %(message)s")

        # Create textLogger
        text_handler = TextHandler(st)
        text_handler.setFormatter(format_log)
        # Logging configuration
        # logging.basicConfig(
        #     filename="test.log",
        #     level=logging.INFO,
        #     format="%(asctime)s - %(levelname)s - %(message)s",
        # )

        # Add the handler to logger
        # logger = logging.getLogger()
        logger.addHandler(text_handler)


def get_app_window_handle(app_name):
    hwnd = win32gui.FindWindow(None, app_name)
    return hwnd


def move_window_to(handle, x, y):
    # Lấy kích thước hiện tại của cửa sổ
    _, _, width, height = win32gui.GetWindowRect(handle)

    # Thay đổi kích thước và vị trí của cửa sổ
    win32gui.SetWindowPos(handle, win32con.HWND_TOP, x, y, width, height, 0)


def main(event=threading.Event()):
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
            if event.is_set():
                logger.info("Stop thread main")
                break
            # print("t dau auto lan: {}".format(n))
            logger.info("Bat dau auto lan: {}".format(n))
            r.round_all(n, event)
            button.exit_game_round20()
            # print("Ket thuc auto lan {}".format(n))
            logger.info("Ket thuc auto lan {}".format(n))
            for t in range(20):
                if event.is_set():
                    logger.info("Stop thread main")
                    break
                t = 20 - t
                # print("Dang cho 5s")
                logger.info(f"Dang cho bat auto lai sau {t}/20s")
                time.sleep(1)

    else:
        logger.info("Khong tim thay cua so co ten {}".format(app_name))


IsOpen = False

t1 = None
t2 = None


def threading_main():
    # Call work function
    global IsOpen, t1, event_main
    if IsOpen is True:
        return
    else:
        IsOpen = True
        t1 = threading.Thread(
            target=test_round,
            args=[
                event_main,
            ],
        )
        t1.start()


def test_round():
    r.test_stop_thread()


def threading_test():
    t2 = threading.Thread(target=stop_thread_main, args=[])
    t2.start()
    # t2.join()


def stop_thread_main():
    global event_main, t1
    event_main.set()
    logger.info("Stop thread main")
    # if t1:
    #     t1.join()
    #     logger.info("Stop thread all")


def gui():
    layout = [[sg.Button("Start Thread"), sg.Button("Stop Thread"), sg.Button("Pause")]]

    window = sg.Window("Thread Demo", layout)

    thread = None
    event_stop = threading.Event()
    event_pause = threading.Event()
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            # exit_event.set()
            r.event_stop.set()
            button.event_stop.set()
            if thread:
                thread.join()
            break
        elif event == "Start Thread" and not thread:
            r.event_stop.clear()
            button.event_stop.clear()
            r.event_pause.set()
            thread = threading.Thread(
                target=r.round_all,
                args=[
                    0,
                ],
            )
            thread.start()
        elif event == "Stop Thread" and thread:
            r.event_pause.set()
            r.event_stop.set()
            button.event_stop.set()
            thread.join()
            thread = None
        elif event == "Pause" and thread:
            logger.info("Pause")
            r.event_pause.clear()
            button.event_pause.clear()
            # thread.join()
            # thread = None

    window.close()


if __name__ == "__main__":
    gui()
    # t1.join()

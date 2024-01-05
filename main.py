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
        if IsOpen is True:
            button1["state"] = "disabled"
        button1.grid(column=0, row=0, sticky="ew")
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
    # global IsOpen
    root = tk.Tk()

    def on_activate():
        # Điều gì đó bạn muốn thực hiện khi phím tắt được kích hoạt
        # print("F9 Hotkey activated!")
        root.destroy()

    def on_closing():
        root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    myGUI(root)
    if IsOpen is False:
        root.button1["state"] = "disabled"
    # t1 = threading.Thread(target=main, args=[])
    # t1.start()
    keyboard.add_hotkey("Ctrl+F9", on_activate)
    keyboard.add_hotkey("Ctrl+q", on_activate)
    keyboard.add_hotkey("Ctrl+F10", threading_main)
    root.mainloop()
    # t1.join()

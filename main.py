import round as r
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
        self.root.title("TEST")
        self.root.option_add("*tearOff", "FALSE")
        self.grid(column=0, row=0, sticky="ew")
        self.grid_columnconfigure(0, weight=1, uniform="a")
        self.grid_columnconfigure(1, weight=1, uniform="a")
        self.grid_columnconfigure(2, weight=1, uniform="a")
        self.grid_columnconfigure(3, weight=1, uniform="a")
        button1 = tk.Button(self, text="Button1", command=threading_main)
        button1.grid(column=0, row=0, sticky="ew")
        # butt
        # Add text widget to display logging info
        st = ScrolledText.ScrolledText(self, state="disabled")
        st.configure(font="TkFixedFont")
        st.grid(column=0, row=1, sticky="w", columnspan=4)

        # Create textLogger
        text_handler = TextHandler(st)

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


IsOpen = False


def threading_main():
    # Call work function
    global IsOpen
    if IsOpen is True:
        return
    else:
        IsOpen = True
        t1 = threading.Thread(target=main, args=[])
        t1.start()


if __name__ == "__main__":
    root = tk.Tk()
    myGUI(root)

    # t1 = threading.Thread(target=main, args=[])
    # t1.start()

    root.mainloop()
    # t1.join()

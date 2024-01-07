import PySimpleGUI as sg
import threading
import win32gui
import win32con
import time
import logging

import round as r
import keyboard
import controller.global_variables as cgv
from controller.filelog import logger, OutputHandler

event = cgv.Event()
gv = cgv.Global_variables()
main_stop = False
main_start = False
appStarted = False
main_pause = False


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
    global main_status
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
            if event.check_event():
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
                if event.check_event():
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
        event.app_start()

        self.t1 = threading.Thread(target=main, args=(), daemon=True)
        self.t1.start()

    def stop(self):
        event.app_stop()
        event.set_event_stop_exit_round()
        self.t1.join()

    def pause(self):
        event.app_pause()


button_pause = "Pause (Ctrl + Space)"


def make_win2():
    global button_pause
    layout = [
        [
            sg.Output(
                key="-OUTPUT-",
                size=(30, 5),
                font="Helvetica 11",
                background_color="black",
                text_color="green",
                sbar_arrow_color="black",
                sbar_background_color="black",
                sbar_frame_color="black",
                sbar_width=0,
                sbar_arrow_width=0,
                sbar_relief="flat",
                # autoscroll=True,
                # border_width=0,
                # disabled=True,
            )
        ],
    ]
    return sg.Window(
        "Second Window",
        layout,
        location=(10, 850),
        finalize=True,
        no_titlebar=True,
        keep_on_top=True,
        background_color="black",
        transparent_color="black",
        # alpha_channel=0.9,
        alpha_channel=0.9,
        border_depth=0,
    )


def make_win1():
    global button_pause
    layout = [
        [
            sg.Button("Start (Ctrl + F9)", key="-START-"),
            sg.Button("Stop (Ctrl + Q)", key="-STOP-", disabled=True),
            sg.Button(button_pause, key="-PAUSE-", disabled=True),
        ],
        [sg.Output(size=(50, 10), key="-OUTPUT-")],
    ]
    return sg.Window(
        "Brodota-bot",
        layout,
        # location=(1000, 400),
        finalize=True,
    )


def gui():
    global main_status, button_pause, main_stop, main_start, appStarted, main_pause
    window1, window2 = make_win1(), None
    appStarted = False
    threadedApp = ThreadedApp()
    log_output1 = OutputHandler(window1)
    logger.addHandler(log_output1)
    while True:
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == "Exit":
            # window.close()
            if window == window2:  # if closing win 2, mark as closed
                window2 = None
            elif window == window1:  # if closing win 1, exit program
                break
        elif (event == "-START-" or main_start is True) and not window2:
            if appStarted is False:
                threadedApp.run()
                window2 = make_win2()  # if main_status is True:
                window1["-START-"].update(disabled=True)
                window1["-PAUSE-"].update(disabled=False)
                window1["-STOP-"].update(disabled=False)
                appStarted = True
            main_start = False

        elif (event == "-STOP-") or (main_stop is True):
            if appStarted is True:
                threadedApp.stop()
                appStarted = False
                main_status = False
                window2.close()
                window2 = None
                window1["-START-"].update(disabled=False)
                window1["-STOP-"].update(disabled=True)
                window1["-PAUSE-"].update(disabled=True)
            main_stop = False
        elif (event == "-PAUSE-") or (main_pause is True):
            if appStarted is True:
                if button_pause == "Pause (Ctrl + Space)":
                    button_pause = "Resume (Ctrl + Space)"
                    window1["-PAUSE-"].update(button_pause)
                    threadedApp.pause()
                else:
                    button_pause = "Pause (Ctrl + Space)"
                    window1["-PAUSE-"].update(button_pause)
                    threadedApp.pause()
            main_pause = False
        elif event == "Emit":
            if window2 is not None:
                window2["-OUTPUT-"].update(values[event] + "\n", append=True)
            window1["-OUTPUT-"].update(values[event] + "\n", append=True)
            # window2.refresh()
        if main_status is True:
            window["-START-"].update(disabled=True)
            window["-PAUSE-"].update(disabled=False)
            window["-STOP-"].update(disabled=False)
        if main_stop is True:
            if appStarted is True:
                threadedApp.stop()
                appStarted = False
                main_status = False
                window2.close()
                window2 = None
                window1["-START-"].update(disabled=False)
                window1["-STOP-"].update(disabled=True)
                window1["-PAUSE-"].update(disabled=True)
            main_stop = False
        if main_start is True:
            if appStarted is False:
                window2 = make_win2()
                threadedApp.run()
                appStarted = True
                main_start = False
        if main_pause is True:
            if appStarted is True:
                if button_pause == "Pause (Ctrl + Space)":
                    button_pause = "Resume (Ctrl + Space)"
                    window1["-PAUSE-"].update(button_pause)
                    threadedApp.pause()
                else:
                    button_pause = "Pause (Ctrl + Space)"
                    window1["-PAUSE-"].update(button_pause)
                    threadedApp.pause()
            main_pause = False

    window.close()


def test1():
    i = 0
    while True:
        if event.check_event():
            break
        i += 1
        logger.debug(f"test1 {i}")
        time.sleep(1)
        if i == 5:
            break


def test2():
    i = 0
    while True:
        if event.check_event():
            break
        i += 1
        logger.debug(f"test2 {i}")
        time.sleep(1)
        break


def main1():
    global main_status
    main_status = True
    test1()
    test2()


def on_hotkey_stop():
    global main_stop
    time.sleep(1)
    if main_stop is False:
        main_stop = True
        logger.debug("Stop thread main")


def on_hotkey_start():
    time.sleep(1)
    global main_start
    if main_start is False:
        main_start = True
        logger.debug("Start thread main")


def on_hotkey_pause():
    time.sleep(1)
    global main_pause
    if main_pause is False:
        main_pause = True
        logger.debug("Pause thread main")


hotkey_combination_start = "ctrl+f9"
hotkey_combination_stop = "ctrl+q"
hotkey_combination_pause = "ctrl+space"
keyboard.add_hotkey(hotkey_combination_stop, on_hotkey_stop)
keyboard.add_hotkey(hotkey_combination_start, on_hotkey_start)
keyboard.add_hotkey(hotkey_combination_pause, on_hotkey_pause)
if __name__ == "__main__":
    # main(pause_event=event_pause, stop_event=event_stop)
    # gui()

    # gui()
    main()
    pass

import threading
import time

import PySimpleGUI as sg
import keyboard
import pydirectinput

import controller.round as r
import interface
from controller.button import Button
from controller.filelog import logger, OutputHandler
from controller.global_variables import global_event, character_moves_event, Dota2

main_stop = False
main_start = False
appStarted = False
main_pause = False
main_status = False
button_pause = "Pause (Ctrl + Space)"
hotkey_combination_start = "ctrl+f9"
hotkey_combination_stop = "ctrl+q"
hotkey_combination_pause = "ctrl+space"
pydirectinput.PAUSE = 0.1


def main():
    global main_status

    hwnd = Dota2.get_app_window_handle()

    if hwnd:
        main_status = True
        global_event.sleep(1)
        Dota2.move_window_to()
        global_event.sleep(1)
        logger.info(f"Tim thay cua so {Dota2.app_name}")
        global_event.sleep(1)
        n = 0
        while True:
            if global_event.check_event():
                # logger.info("Stop thread main")
                break
            n += 1
            # print("t dau auto lan: {}".format(n))
            logger.info("Bat dau auto lan: {}".format(n))
            if r.round_all(n) is False:
                break
            if Button.exit_game_round20() is False:
                break
            logger.info("Ket thuc auto lan {}".format(n))
            for t in range(10):
                if global_event.check_event():
                    break
                t = 10 - t
                # print("Dang cho 5s")
                logger.info(f"Dang cho bat auto lai sau {t}/10s")
                global_event.sleep(1)

    else:
        main_status = False
        logger.info("Khong tim thay cua so co ten {}".format(Dota2.app_name))


class ThreadedApp:
    def __init__(self):
        self.t1 = threading.Thread()

    def run(self):
        global_event.app_start()
        character_moves_event.app_start()
        self.t1 = threading.Thread(target = main, args = (), daemon = True)
        self.t1.start()

    def stop(self):
        global_event.app_stop()
        character_moves_event.app_stop()
        self.t1.join()

    @staticmethod
    def pause():
        global_event.app_pause()
        character_moves_event.app_pause()

    @staticmethod
    def resume():
        global_event.app_resume()
        character_moves_event.app_resume()


def make_win1():
    global button_pause
    # sg.theme("SystemDefaultForReal")
    menu_def = [["Config", ["Auto", "Item", "Hero"]]]

    layout = [[sg.Menu(menu_def, tearoff = False)],
              [sg.Output(size = (50, 15), key = "-OUTPUT-")],
              [sg.Button("Start (Ctrl + F9)", key = "-START-"),
               sg.Button("Stop (Ctrl + Q)", key = "-STOP-", disabled = True),
               sg.Button(button_pause, key = "-PAUSE-", disabled = True), ], ]
    return sg.Window("Brodota-bot", layout, finalize = True)


def gui():
    global main_status, button_pause, main_stop, main_start, appStarted, main_pause
    window = make_win1()
    appStarted = False
    threaded_app = ThreadedApp()
    log_output1 = OutputHandler(window)
    logger.addHandler(log_output1)

    while True:
        event, values = window.read(timeout = 100)
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-START-" or main_start is True:
            if appStarted is False:
                threaded_app.run()
                # if main_status is True:
                window["-START-"].update(disabled = True)
                window["-PAUSE-"].update(disabled = False)
                window["-STOP-"].update(disabled = False)
                appStarted = True
            main_start = False

        elif (event == "-STOP-") or (main_stop is True):
            if appStarted is True:
                threaded_app.stop()
                appStarted = False
                main_status = False
                window["-START-"].update(disabled = False)
                window["-STOP-"].update(disabled = True)
                window["-PAUSE-"].update(disabled = True)
            main_stop = False
        elif (event == "-PAUSE-") or (main_pause is True):
            if appStarted is True:
                if button_pause == "Pause (Ctrl + Space)":
                    button_pause = "Resume (Ctrl + Space)"
                    window["-PAUSE-"].update(button_pause)
                    threaded_app.pause()
                else:
                    button_pause = "Pause (Ctrl + Space)"
                    window["-PAUSE-"].update(button_pause)
                    threaded_app.resume()
            main_pause = False
        elif event == "Auto":
            # logger.info("Auto")
            interface.window_config_auto()

        elif event == "Emit":
            window["-OUTPUT-"].update(values[event] + "\n", append = True)
        if main_status is True:
            window["-START-"].update(disabled = True)
            window["-PAUSE-"].update(disabled = False)
            window["-STOP-"].update(disabled = False)
            main_status = False
    window.close()


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


if __name__ == "__main__":

    keyboard.add_hotkey(hotkey_combination_stop, on_hotkey_stop)
    keyboard.add_hotkey(hotkey_combination_start, on_hotkey_start)
    keyboard.add_hotkey(hotkey_combination_pause, on_hotkey_pause)

    gui()
    # main()
    # print(config.sections())
    # print(read_config("ConfigAuto", "MyBurn"))
    # save_config("move", "100")
    pass

import configparser
import os
import threading
import time

import pydirectinput
import PySimpleGUI as sg

from controller.filelog import OutputHandler, logger
from controller.global_variables import Dota2, character_moves_event, global_event, path

config = configparser.ConfigParser()
path_config = path.get_absolute_path(os.path.join("interface", "config.ini"))
config.read(path_config)
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

def save_config(key, value):
    config["ConfigAuto"][key] = value
    with open(path_config, "w") as config_file:
        config.write(config_file)


def read_config(section, key):
    global config
    return config[section][key]


move_status = False
like_status = False

item_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
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
        self.t1 = threading.Thread(target=main, args=(), daemon=True)
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


def gui():
    global main_status, button_pause, main_stop, main_start, appStarted, main_pause

    appStarted = False
    threaded_app = ThreadedApp()
    log_output1 = OutputHandler(window)
    logger.addHandler(log_output1)


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
class ThreadedApp:
    def __init__(self):
        self.t1 = threading.Thread()

    def run(self):
        global_event.app_start()
        character_moves_event.app_start()
        self.t1 = threading.Thread(target=main, args=(), daemon=True)
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
def window_config_auto():
    sg.theme("SystemDefaultForReal")
    global move_status, like_status
    if read_config("ConfigAuto", "Move") == "1":
        move_status = True
    if read_config("ConfigAuto", "Like") == "1":
        like_status = True
    item = read_config("ConfigAuto", "Burn")
    layout_column1 = [
        [
            sg.Checkbox(
                "Di chuyển tự động",
                default=move_status,
                key="-Move-",
                enable_events=True,
                size=(20, 1),
                auto_size_text=True,
            )
        ],
        [
            sg.Checkbox(
                "Tắt like khi thoát game",
                default=like_status,
                key="-Like-",
                enable_events=True,
                size=(20, 1),
                auto_size_text=True,
            )
        ],
    ]
    layout_column2 = [
        [
            sg.Radio(
                "Di Mine",
                group_id="1",
            )
        ],
        [sg.Radio("Di Devil's Grave", group_id="1")],
    ]
    layout_column3 = [
        [
            sg.Text("Độ khó Burn:"),
            sg.Combo(item_list, default_value=item, key="-Item-", pad=(0, 0)),
        ],
    ]
    layout_column4 = [
        [sg.Button("Save", key="-Save-")],
    ]
    layout = [
        [
            sg.Column(layout_column1, vertical_scroll_only=True),
            sg.Column(layout_column2, vertical_scroll_only=True),
        ],
        [sg.Column(layout_column3, vertical_scroll_only=False)],
        [sg.Column(layout_column4, vertical_scroll_only=False,
                   justification="right")],
    ]
    window1 = sg.Window("Config auto", layout, finalize=True)
    choice = None
    while True:
        event, values = window1.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "-Save-":
            save_config("move", str(values["-Move-"]))
            logger.info(f"Save config tu dong di chuyen: {
                        str(values['-Move-'])}")
            save_config("like", str(values["-Like-"]))
            logger.info(f"Save config tat like khi thoat game: {
                        str(values['-Like-'])}")
            save_config("burn", str(values["-Item-"]))
            logger.info(f"Save config burn: {str(values['-Item-'])}")
            window1.close()
            break

def main_window():
    global main_status, button_pause, main_stop, main_start, appStarted, main_pause
    sg.theme("SystemDefaultForReal")
    menu_def = [["Config", ["Auto", "Item", "Hero"]]]

    layout = [
        [sg.Menu(menu_def)],
        [sg.Output(key="-OUTPUT-")],
        [
            sg.Button("Start (Ctrl + F9)", key="-START-"),
            sg.Button("Stop (Ctrl + Q)", key="-STOP-", disabled=True),
            sg.Button("button_pause", key="-PAUSE-", disabled=True),
        ],
        [
            sg.Checkbox(
                "Tắt like khi thoát game",
                default=True,
                key="-Like-",
            ),
        ],
    ]
    appStarted = False
    threaded_app = ThreadedApp()
    
    window= sg.Window("Brodota-bot", layout, finalize=True)
    log_output1 = OutputHandler(window)
    logger.addHandler(log_output1)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Exit":
            break
        elif event == "-START-" or main_start is True:
            if appStarted is False:
                threaded_app.run()
                # if main_status is True:
                window["-START-"].update(disabled=True)
                window["-PAUSE-"].update(disabled=False)
                window["-STOP-"].update(disabled=False)
                appStarted = True
            main_start = False

        elif (event == "-STOP-") or (main_stop is True):
            if appStarted is True:
                threaded_app.stop()
                appStarted = False
                main_status = False
                window["-START-"].update(disabled=False)
                window["-STOP-"].update(disabled=True)
                window["-PAUSE-"].update(disabled=True)
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
            window_config_auto()

        elif event == "Emit":
            window["-OUTPUT-"].update(values[event] + "\n", append=True)
        if main_status is True:
            window["-START-"].update(disabled=True)
            window["-PAUSE-"].update(disabled=False)
            window["-STOP-"].update(disabled=False)
            main_status = False
    window.close()
if __name__ == "__main__":
    # window_config_auto()
    print(path_config)
    pass

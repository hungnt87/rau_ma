import configparser

import PySimpleGUI as sg
from controller.filelog import logger
config = configparser.ConfigParser()
config.read("config.ini")


def save_config(key, value):

    config["ConfigAuto"][key] = value
    with open("config.ini", 'w') as config_file:
        config.write(config_file)


def read_config(section, key):
    global config
    return config[section][key]


move_status = False
like_status = False

item_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def window_config_auto():
    global move_status, like_status
    if read_config("ConfigAuto", "Move") == "1":
        move_status = True
    if read_config("ConfigAuto", "Like") == "1":
        like_status = True
    item = read_config("ConfigAuto", "Burn")
    layout_column1 = [
        [sg.Checkbox("Di chuyển tự động", default = move_status, key = "-Move-", enable_events = True, size = (20, 1),
                     auto_size_text = True, )],
        [sg.Checkbox("Tắt like khi thoát game", default = like_status, key = "-Like-", enable_events = True,
                     size = (20, 1),
                     auto_size_text = True, )]]
    layout_column2 = [
        [sg.Radio("Di Mine", group_id = "1", )],
        [sg.Radio("Di Devil's Grave", group_id = "1")]
        ]
    layout_column3 = [
        [sg.Text("Độ khó Burn:"),
         sg.Combo(item_list, default_value = item, key = "-Item-", pad = (0, 0))],
        ]
    layout_column4 = [
        [sg.Button("Save", key = "-Save-")], ]
    layout = [
        [sg.Column(layout_column1, vertical_scroll_only = True),
         sg.Column(layout_column2, vertical_scroll_only = True)],
        [sg.Column(layout_column3, vertical_scroll_only = False)],
        [sg.Column(layout_column4, vertical_scroll_only = False, justification = 'right')]

        ]
    window1 = sg.Window("Config auto", layout, finalize = True)
    choice = None
    while True:
        event, values = window1.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "-Save-":

            save_config("move", str(values['-Move-']))
            logger.info(f"Save config tu dong di chuyen: {str(values['-Move-'])}")
            save_config("like", str(values['-Like-']))
            logger.info(f"Save config tat like khi thoat game: {str(values['-Like-'])}")
            save_config("burn", str(values["-Item-"]))
            logger.info(f"Save config burn: {str(values['-Item-'])}")
            window1.close()
            break


if __name__ == '__main__':
    window_config_auto()

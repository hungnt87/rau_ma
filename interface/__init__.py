import PySimpleGUI as sg

from controller.filelog import logger
from controller.global_variables import config

move_status = False
like_status = False

item_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def window_config_auto():
    # sg.theme("SystemDefaultForReal")
    global move_status, like_status
    if config.read_config("AutoConfig", "move") == "True":
        move_status = True
    else:
        move_status = False
    if config.read_config("AutoConfig", "like") == "True":
        like_status = True
    else:
        like_status = False
    item = config.read_config("AutoConfig", "burn")
    layout_column1 = [
        [
            sg.Checkbox(
                "Di chuyển tự động",
                default=move_status,
                key="-Move-",
                enable_events=True,
                auto_size_text=True,
                size=(20, 20),
            )
        ],
        [
            sg.Checkbox(
                "Tắt like khi thoát game",
                default=like_status,
                key="-Like-",
                enable_events=True,
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
            sg.Combo(item_list, default_value=item, key="-Item-"),
        ],
    ]
    layout_column4 = [
        [sg.Button("Save", key="-Save-")],
    ]
    layout = [
        [
            sg.Column(
                layout_column1,
                vertical_scroll_only=True,
            ),
            sg.Column(layout_column2, vertical_scroll_only=True),
        ],
        [sg.Column(layout_column3, vertical_scroll_only=False)],
        [sg.Column(layout_column4, vertical_scroll_only=False, justification="right")],
    ]
    window1 = sg.Window(
        "Config auto",
        layout,
        element_padding=(10, 10),
        auto_size_text=True,
    )
    choice = None
    while True:
        event, values = window1.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "-Save-":
            config.save_config("AutoConfig", "move", str(values["-Move-"]))
            logger.info(f"Save config tu dong di chuyen: {str(values['-Move-'])}")
            config.save_config("AutoConfig", "like", str(values["-Like-"]))
            logger.info(f"Save config tat like khi thoat game: {str(values['-Like-'])}")
            config.save_config("AutoConfig", "burn", str(values["-Item-"]))
            logger.info(f"Save config burn: {str(values['-Item-'])}")
            window1.close()
            break


if __name__ == "__main__":
    window_config_auto()
    # main_window()
    pass

import PySimpleGUI as sg

from controller.filelog import logger
from controller.global_variables import config

move_status = False
like_status = False

item_list = tuple(str(i * 10) for i in range(0, 21))
config_burn = 0


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
    if config.read_config("AutoConfig", "config_burn") == "0":
        config_burn = 0
    elif config.read_config("AutoConfig", "config_burn") == "1":
        config_burn = 1
    elif config.read_config("AutoConfig", "config_burn") == "2":
        config_burn = 2
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
                tooltip="Yêu cầu cài đặt chế độ di chuyển trong game bằng chuột trước",
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
            sg.Radio(
                "Tự chọn Burn trong game:",
                key="Radio_0",
                group_id="2",
                default=(config_burn == 0),
            )
        ],
        [
            sg.Radio(
                "Burn tăng từ min",
                key="Radio_min",
                group_id="2",
                default=(config_burn == 1),
            )
        ],
        [
            sg.Radio(
                "Burn giảm từ max",
                key="Radio_max",
                group_id="2",
                default=(config_burn == 2),
            )
        ],
        [
            sg.Text("Độ khó Burn:"),
            sg.Combo(
                item_list, default_value=item, key="-Item-", readonly=True, size=(5, 1)
            ),
        ],
    ]

    layout_column5 = [
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
        [
            sg.Column(layout_column3, vertical_scroll_only=True, justification="left"),
        ],
        [sg.Column(layout_column5, vertical_scroll_only=False, justification="right")],
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
            if values["Radio_0"]:
                config.save_config("AutoConfig", "config_burn", "0")
                logger.info(f"Chọn config burn trong game")
            elif values["Radio_min"]:
                config.save_config("AutoConfig", "config_burn", "1")
                logger.info(f"Save config burn giảm từ max")
            elif values["Radio_max"]:
                config.save_config("AutoConfig", "config_burn", "2")
                logger.info(f"Save config burn tăng từ min")
            window1.close()
            break


if __name__ == "__main__":
    window_config_auto()
    # main_window()
    pass

import logging

import PySimpleGUI as sg


class OutputHandler(logging.Handler):
    # window: sg.Window

    def __init__(self, window: sg.Window):
        super().__init__()
        self.window = window

    def emit(self, record):
        self.window.write_event_value("Emit", record.msg)


logger = logging.getLogger(__name__)

path_log = "log.log"
file_logger = logging.FileHandler(path_log, mode="w", encoding="utf-8")
new_format = "[%(asctime)s] - [%(levelname)s] - %(message)s"

file_logger_format = logging.Formatter(new_format)
console_format = logging.Formatter(new_format)
file_logger.setFormatter(file_logger_format)

logger.addHandler(file_logger)
logger.setLevel(logging.ERROR)

# print(path)
# now we can add the console logging
console = logging.StreamHandler()
console.setFormatter(console_format)
console.setLevel(logging.DEBUG)
logging.getLogger(__name__).addHandler(console)

import logging
import os
import sys
import controller.global_variables as cgv

# gv = cgv.Global_variables()


class TextHandler(logging.Handler):
    def __init__(self, elem):
        logging.Handler.__init__(self)
        self.elem = elem

    def emit(self, record):
        log_message = self.format(record)
        color = self.get_log_color(record.levelname)
        self.elem.print(log_message, text_color=color)

    def get_log_color(self, levelname):
        # Xác định màu chữ dựa trên levelname (ví dụ: WARNING màu vàng)
        if levelname == "WARNING":
            return "green"
        elif levelname == "ERROR":
            return "red"
        elif levelname == "CRITICAL":
            return "red"
        else:
            return None


# def resource_path(relative_path):
#     """Get absolute path to resource, works for dev and for PyInstaller"""
#     base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)


path = "log.log"
path = cgv.resource_path(path)
# create the logging instance for logging to file only
logger = logging.getLogger(__name__)

# create the handler for the main logger
file_logger = logging.FileHandler(path)
NEW_FORMAT = "[%(asctime)s] - [%(levelname)s] - %(message)s"
format_log = "%(asctime)s\t %(levelname)s\t %(message)s"

file_logger_format = logging.Formatter(format_log)

# tell the handler to use the above format
file_logger.setFormatter(file_logger_format)
console_format = logging.Formatter(NEW_FORMAT)
# finally, add the handler to the base logger
logger.addHandler(file_logger)

# remember that by default, logging will start at 'warning' unless
# we set it manually
logger.setLevel(logging.DEBUG)

# print(path)
# now we can add the console logging
# console = logging.StreamHandler()
# console.setFormatter(console_format)
# console.setLevel(logging.DEBUG)
# logging.getLogger(__name__).addHandler(console)

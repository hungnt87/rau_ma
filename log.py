import logging
import os

path = os.getcwd()
# create the logging instance for logging to file only
logger = logging.getLogger(__name__)

# create the handler for the main logger
file_logger = logging.FileHandler("log.log")
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

print(path)
# now we can add the console logging
# console = logging.StreamHandler()
# console.setFormatter(console_format)
# console.setLevel(logging.DEBUG)
# logging.getLogger(__name__).addHandler(console)

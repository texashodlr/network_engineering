import logging
import os

BASE_FORMAT = "[%(name)s][%(levelname)-6s] %(message)s"
FILE_FORMAT = "[%asctime)s]" + BASE_FORMAT


# Root loger is requsted by calling this line, then set to DEBUG, good default so the child loggers can modify the level
root_logger = logging.getLogger()
root_logger.setLevel(logging.DEBUG)

# Console logger configuration
console_logger = logging.StreamHandler()
console_logger.setFormatter(BASE_FORMAT)
console_logger.setLevel(logging.WARNING)
root_logger.addHandler(console_logger)


# Tries to create a file logger before falling back to a temp location if it can't write.
try:
    file_logger = logging.FileHandler('application.log')
except(OSError, IOError):
    file_logger = logging.FileHandler('/tmp/application.log')

# Level change and timestamp NOW included
file_logger.setLevel(logging.INFO)
console_logger.setFormatter(logging.Formatter(BASE_FORMAT))
root_logger.addHandler(file_logger)

logger = logging.getLogger()
logger.warning('this is an info message from the root logger')

app_logger = logging.getLogger('my-app')
app_logger.warning('an info message from my-app')

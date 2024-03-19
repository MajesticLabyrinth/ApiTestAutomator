# This is a sample Python script.
import logging

from core.logger import Logger

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    log = Logger('output.log', level='debug')
    log_error = Logger('output.log', level='error')

    log.logger.info('This is informational message')
    log.logger.debug('This is debug message from log.logger')
    log.logger.critical('This is critical message from log.logger')
    log.logger.error('This is error message from log.logger')
    log.logger.warning('This is warning message from log.logger')
    log.logger.exception('This is exception message from log.logger')
    log.logger.log(logging.CRITICAL,'This is a simple log message from log.logger')

    log_error.logger.info('This is informational message 2')
    log_error.logger.debug('This is informational message 2 from log_error')
    log_error.logger.critical('This is critical informational message 2 from log_error')
    log_error.logger.error('This is error message 2 from log_error')
    log_error.logger.warning('This is warning message 2 from log.logger')
    log_error.logger.exception('This is exception message 2 from log.logger')
    log_error.logger.log(logging.CRITICAL,'This is a simple log message 2 from log.logger')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

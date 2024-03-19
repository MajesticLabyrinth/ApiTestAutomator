import logging
from logging import handlers

# Log level mappings
class Logger(object):
    level_relations = {
        'debug' : logging.DEBUG,
        'info' : logging.INFO,
        'warning' : logging.WARNING,
        'error' : logging.ERROR,
        'crit' : logging.CRITICAL
    }

    def __init__(self, filename, level='info', when='D', backCount = 3,
                 fmt = '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt) # Setting the log format
        self.logger.setLevel(self.level_relations.get(level)) # Setting the log level
        console_handler = logging.StreamHandler() # on-screen output
        console_handler.setFormatter(format_str) # Setting the format
        th = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount, encoding='utf-8')   # Automatically generates the file at specified interval
        th.setFormatter(format_str)
        #self.logger.addHandler(sh) # Add the object to the logger
        self.logger.addHandler(th)
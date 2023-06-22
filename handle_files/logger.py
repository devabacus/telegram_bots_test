import logging
from colorama import init, Fore, Style

# Инициализация colorama
init()

# Цвета для разных уровней логирования
COLORS = {
    'DEBUG': Fore.BLUE,    # синий
    'INFO': Fore.GREEN,     # зеленый
    'WARNING': Fore.YELLOW,  # желтый
    'ERROR': Fore.RED,    # красный
    'CRITICAL': Fore.MAGENTA  # пурпурный
}

class ColoredConsoleHandler(logging.StreamHandler):
    def emit(self, record):
        message = self.format(record)
        color = COLORS.get(record.levelname, '')
        self.stream.write(color + message + Style.RESET_ALL + "\n")
        self.flush()

class Logger:

    def __init__(self, name, filename=""):
        self.logger = logging.getLogger(name)
        self.clear_handlers()  # Удаляем все предыдущие обработчики
        self.logger.setLevel(logging.INFO)

        if len(filename) > 0:
            handler = logging.FileHandler(filename, encoding='utf-8')
        else:
            handler = ColoredConsoleHandler()
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        handler.setLevel(logging.INFO)

        self.logger.addHandler(handler)

    def clear_handlers(self):
        for handler in self.logger.handlers[:]:
            self.logger.removeHandler(handler)

    def get_logger(self):
        return self.logger
    
    
# log = Logger(__name__).get_logger()
# logf = Logger(__name__, filename="file.log").get_logger()
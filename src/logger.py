import datetime
import os


class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)
        return cls._instance[cls]


class Logger(metaclass=MetaSingleton):
    @staticmethod
    def _write_file(type_log, msg: str):
        if not os.path.exists('log'):
            os.mkdir('log')
        log_write = f'[{type_log}] [{str(datetime.datetime.now())}]: {msg}\n'
        print(log_write)
        with open(f'log/{datetime.date.today()}.log', 'a') as file_log:
            file_log.write(log_write)

    def info(self, msg):
        self._write_file('Info', msg)

    def error(self, msg):
        self._write_file('Error', msg)

    def warning(self, msg):
        self._write_file('Warning', msg)

    def debug(self, msg):
        self._write_file('Debug', msg)

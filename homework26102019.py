
import time
class Logger:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode

    def __enter__(self):
        self.file = open(self.path, self.mode)
        return self

    def write(self, value):
        self.file.write(f'{time.ctime()} {value}\n')

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self.file.close()

with Logger('files/log.txt', 'w') as logger:
    logger.write(12 + 14)
    logger.write('Hello World')
    logger.write(True)


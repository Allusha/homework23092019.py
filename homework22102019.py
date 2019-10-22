#1 task

from functools import wraps


class TypeDecorators:

    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args):
            return int(*args)
        return wrapper

    @staticmethod
    def to_bool(func):
        @wraps(func)
        def wrapper(string):
            if string == 'True':
                return True
            if string == 'False':
                return False
            else:
                return "Error"
        return wrapper

    @staticmethod
    def to_str(func):
        @wraps(func)
        def wrapper(*args):
            return str(*args)
        return wrapper

    @staticmethod
    def to_float(func):
        @wraps(func)
        def wrapper(*args):
            return float(*args)
        return wrapper


@TypeDecorators.to_float
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


#2 task 
# not complited

class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self.workers = []


    def add_worker(self, worker):
        if isinstance(worker, Worker):
            self.workers.append(worker)
        else:
            print("Error")



class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss
        boss.add_worker(self)

    def __repr__(self):
        return self.name

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss):
        if new_boss is isinstance(new_boss, Boss):
            return new_boss



class Stack:
    def __init__(self, maxsize=0):
        self.__dict = {}
        self.maxsize = maxsize

    def push(self, key: str, value):
        if len(self.__dict) < self.maxsize:
            self.__dict[key] = value
        else:
            return 'Dict is full'

    def pop(self):
        self.__dict.popitem()

    def reverse(self):
        dict_copy = self.__dict.copy()
        dict_reverse = {}
        for _ in range(len(dict_copy)):
            a = dict_copy.popitem()
            dict_reverse[a[0]] = a[1]
        return dict_reverse

    def reverse_in_place(self):
        self.__dict = self.reverse()

    def join(self, joiner: str) -> str:
        d_copy = self.__dict.copy()
        string_dict = ''
        a = d_copy.popitem()
        for value in d_copy.values():
            string_dict += f'{value}{joiner}'
        string_dict += f'{a[1]}'
        return string_dict

    def index(self, item):
        dict_list = []
        for value in self.__dict.values():
            dict_list.append(value)
        for index, i in enumerate(dict_list):
            if i == item:
                return index

    def last_index(self, item):
        pass

    def sum(self):
        result = 0
        for value in self.__dict.values():
            if not isinstance(value, int):
                raise TypeError('You cannot sum non integer objects')
            result += value
        return result

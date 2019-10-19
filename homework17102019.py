#1 task


def logger(func):
    def wrapped(*args):
        print(f'{func.__name__} called with {args}')

    return wrapped


@logger
def add(x, y):
    return x + y


add(4, 5)


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


#2 task


def stop_words(words: list):
    def decorator(func):
        def wrapped(*args):
            string = func(*args)
            for word in words:
                return string.replace(word ,'*')

        return wrapped

    return decorator



@stop_words(['pepsi', 'BMW'])
def create_slogan(name: str) -> str:
    return f"{name} drinks pepsi in his brand new BMW!"

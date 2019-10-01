# first task
def insert_whitespace(string):
    new_string = []
    for l in string:
        if l.isupper():
            new_string.append(f'{" "}{l}')
        else:
            new_string.append(l)
    result = ''.join(new_string)

    return result

# second task
def calculator(a, b, operation):
    operation_map = {
        'sum': a + b,
        'min': a - b,
        'dev': a / b,
        'mul': a * b
    }

    return operation_map[operation]

# third task
def wrap(line, n):
    print([line[i:i + n] for i in range(0, len(line), n)])

    return line

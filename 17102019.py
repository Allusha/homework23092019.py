
#not all

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    if not all (num > 0 for num in nums):
       print(func2(nums))
    else:
       print(func1(nums))


# if any

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    if any (num < 0 for num in nums):
       print(func2(nums))
    else:
       print(func1(nums))



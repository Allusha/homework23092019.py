#task 1
#almost working 

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    result = []
    positives = []
    if positives:
        result.append(func1(positives))
    else:
        result.append(func2(nums))
    return result


#working

def square_nums(nums):
    return [num ** 2 for num in nums]

def remove_negatives(nums):
    return [num for num in nums if num > 0]


def choose_func(nums: list, func1, func2):
    result = []
    if any(map(lambda x: x<0, nums)):
        result.append(func2(nums))
    else:
        result.append(func1(nums))
    return result

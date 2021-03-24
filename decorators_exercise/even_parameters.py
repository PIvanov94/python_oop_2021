def is_even(*args):
    try:
        for a in args:
            if a % 2 != 0:
                return False
        return True
    except TypeError:
        return False


def even_parameters(func):
    def wrapper(*args):
        if not is_even(*args):
            return "Please use only even numbers!"
        return func(*args)

    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

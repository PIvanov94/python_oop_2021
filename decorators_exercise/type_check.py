def type_check(type_to_check):
    def decorator(func):
        def wrapper(*args):
            if all(isinstance(a, type_to_check) for a in args):
                return func(*args)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))
print(times2('Not A Number'))

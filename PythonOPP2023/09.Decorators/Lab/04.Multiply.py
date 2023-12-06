def multiply(times: int):
    def decorator(function):
        def wrapper(*args, **kwargs):
            func_result = function(*args, **kwargs)
            return func_result * times
        return wrapper
    return decorator


@multiply(5)
def add_ten(number: int):
    return number + 10


print(add_ten(6))

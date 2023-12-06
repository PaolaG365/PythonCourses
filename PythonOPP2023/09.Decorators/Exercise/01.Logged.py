def logged(function):
    def wrapper(*args, **kwargs):
        # func_res = function(*args, **kwargs)
        # name_func = function.__name__
        # arg_func = (*args, *kwargs)
        return f"you called {function.__name__}{(*args, *kwargs)}\nit returned {function(*args, **kwargs)}"
    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))


@logged
def another_func(**kwargs):
    return [(key, value) for key, value in kwargs.items()]


print(another_func(key=1, name="first test user", password="random password"))

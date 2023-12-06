class store_results:
    _FUNCTIONS_RESULTS = "results.txt"

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        with open(store_results._FUNCTIONS_RESULTS, "a") as file:
            file.write(f"Function {self.function.__name__} was called. Result: {self.function(*args, **kwargs)}\n")


@store_results
def add(a, b):
    return a + b


@store_results
def mult(a, b):
    return a * b


@store_results
def info(**kwargs):
    return [(k, v) for k, v in kwargs.items()]


add(2, 2)
mult(6, 4)
info(name="Penka", age=25)

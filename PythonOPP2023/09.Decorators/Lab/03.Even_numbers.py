def even_numbers(function):

    def wrapper(numbers):
        # result = []
        # for num in numbers:
        #     if num % 2 == 0:
        #         result.append(num)

        return [num for num in numbers if num % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))

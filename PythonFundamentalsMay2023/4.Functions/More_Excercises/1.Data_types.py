
# def int_input(n): return n * 2
#
#
# def real_input(n): return n * 1.5  # float
#
#
# def string_input(n): return "$" + n + "$"
#
#
# input_type = input()
# actual_input = input()
#
# if input_type == "int":
#     print(int_input(int(actual_input)))
#
# elif input_type == "real":
#     print(f"{real_input(float(actual_input)):.2f}")
#
# elif input_type == "string":
#     print(string_input(actual_input))


# second way

def data_types(n, data="str"):

    if data == "int":
        return int(n) * 2

    elif data == "real":  # floating point num
        return f"{float(n) * 1.5:.2f}"

    elif data == "string":
        return "$" + n + "$"


input_type = input()
actual_input = input()
print(data_types(actual_input, data=input_type))

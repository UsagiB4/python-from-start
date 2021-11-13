# in python function is a first class object.
# which means you can pass a function in another function like parameter or variable.

def get_int_as_str(numb):
    return str(numb)


def print_int(a_function, numb):
    print(a_function(numb))
    return


print_int(get_int_as_str, 12)

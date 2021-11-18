# in python function is a first class object.
# which means you can pass a function in another function like parameter or variable.

def get_int_as_str(numb):
    return str(numb)


def print_int(a_function, numb):
    print(a_function(numb))
    return


#  print_int(get_int_as_str, 12)

# Decorator is a type of function that extends another functions functionality
# without modifying it.

def a_decorator(a_func):
    def add_hello():
        str_to_add = "Hello"
        a_func(str_to_add)

        return
    return add_hello()


@a_decorator
def say_name(a):
    print(a,"Tasif")
    return


"""
Already implemented in python
"""


def main_function(text):
    return "Passed into main function : {}".format(text)


def decorate(func):
    def func_wrapper(name):
        return "Before  {0}   After".format(func(name))

    return func_wrapper


my_get_text = decorate(main_function)

print(my_get_text("John"))

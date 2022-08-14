"""
A decorator is a function that takes another function as an argument,
and extends its behavior without changing the original function explicitly.

In general, a decorator is:

A function that takes another function (original function) as an argument and returns another function (or closure)
The closure typically accepts any combination of positional and keyword-only arguments.
The closure function calls the original function using the arguments passed to the closure and returns the result of the function.
"""


def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


def currency(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'

    return wrapper


net_price = currency(net_price)
print(net_price(100, 0.05))

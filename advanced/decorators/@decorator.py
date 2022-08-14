"""
A decorator is a function that changes the behavior of another function without explicitly modifying it.
Use the @ symbol to decorate a function.
Use the wraps function from the functools built-in module to retain the documentation and name of the original function.
"""
from functools import wraps


def currency(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return f'${result}'
    return wrapper


@currency
def net_price(price, tax):
    """ calculate the net price from price and tax
    Arguments:
        price: the selling price
        tax: value added tax or sale tax
    Return
        the net price
    """
    return price * (1 + tax)


print(net_price(100, 0.05))

from functools import wraps


def repeat(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        for _ in range(5):
            result = fn(*args, **kwargs)
        return result

    return wrapper


@repeat
def say(message):
    '''
    print the message
    Arguments
        message: the message to show
    '''
    print(message)


say('Hello')

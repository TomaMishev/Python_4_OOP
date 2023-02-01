# Create three decorators: make_bold, make_italic, make_underline, which will have to wrap a text returned from a
# function in <b></b>, <i></i> and <u></u> respectively.


def make_underline(func_ref):
    def wrapper(*args):
        func = func_ref(*args)
        return f"<u>{func}</u>"
    return wrapper


def make_italic(func_ref):
    def wrapper(*args):
        func = func_ref(*args)
        return f"<i>{func}</i>"
    return wrapper


def make_bold(func_ref):
    def wrapper(*args):
        func = func_ref(*args)
        return f"<b>{func}</b>"
    return wrapper





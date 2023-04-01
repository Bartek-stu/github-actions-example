from mathtools import logger

def require_numeric_values(func):
    def inner(*args, **kwargs):
        for arg in args:
            if type(arg) != int and type(arg) != float:
                logger.error("Provide numeric values")
                raise TypeError(f"Values must be numeric")
        return func(*args, **kwargs)
    return inner
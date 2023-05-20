import doctest

def add(x , y):
    """
    >>> add (3 , 5)
    8
    """
    return x + y

def subtract(x , y):
    """
    >>> subtract (3 , 5)
    -2
    """
    return x - y

def multiply(x , y):
    """
    >>> multiply (3 , 5)
    15
    """
    return x * y

def division(x , y):
    """
    >>> division (10 , 2)
    5.0
    """
    return x / y


if __name__ == '__main__':
    doctest.testmod()

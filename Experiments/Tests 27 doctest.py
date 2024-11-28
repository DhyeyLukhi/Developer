def add(a, b):
    """
    This function adds two numbers together.

    >>> add(2, 3)
    5
    >>> add(0, 0)
    0
    >>> add(-1, 1)
    0
    >>> print(eval(str(-6+6)))
    0
    """
    return a + b


if __name__ == "__main__":
    import doctest
    doctest.testmod()

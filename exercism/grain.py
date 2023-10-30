def square(number):
    if number >= 1 and number <= 64 :
        return 2 ** (number - 1)
    else:
        raise ValueError("Value not on the chessboard")
    pass


def total():
    return sum([square(i) for i in range(1,65)])
    pass


"""
    if not 64 >= number > 0:
        raise ValueError("square must be between 1 and 64")
    else:
        return 2 ** (number - 1)
        """
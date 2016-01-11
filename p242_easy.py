# https://www.reddit.com/r/dailyprogrammer/comments/3twuwf/
# Problem follows a bisection of Fibonacci seqence, A001906


def fruitGen():
    """ output: (week, fruit)"""
    i, a, b = 2, 1, 2

    yield (1, 0)

    while True:
        yield (i, a)
        a += b
        b += a
        i += 1


def plant(x, y):
    """
        Finds how many weeks it needs to support x people
        input: (# of people, starting fruits)
    """

    for i, k in fruitGen():
        if k * y >= x:
            return i

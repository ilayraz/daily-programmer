# https://www.reddit.com/r/dailyprogrammer/comments/3uuhdk/
# Expects file called 'input.txt' in same directory

from math import sqrt


def sumFactors(n):
    step = 2 if n % 2 else 1
    result = set()

    for i in range(1, int(sqrt(n)), step):
        div, mod = divmod(n, i)
        if not mod:
            result |= {i, div}

    return sum(result)


def main():
    for n in open('input.txt').readlines():
        n = int(n)
        deficiency = 2*n - sumFactors(n)

        if deficiency > 0:
            print('%d deficient' % n)
        elif deficiency < 0:
            print('%d abundant by %d' % (n, abs(deficiency)))
        else:
            print('%d ~~neither~~' % n)

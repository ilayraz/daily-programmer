# https://www.reddit.com/r/dailyprogrammer/comments/4savyr/


from itertools import combinations
from functools import reduce


def checkElement(longN, short, length=2):
    if len(short) != length and not longN.isalpha() and not short.isalpha():
        return False

    for letter in short:
        try:
            longN = longN[longN.index(letter) + 1:]
        except ValueError:
            return False
    return True


def allShorts(longN, length=2):
    return list(set(filter(
        lambda short: checkElement(longN, ''.join(short), length),
        combinations(longN, length)
    )))


def findShortName(longN, length=2):
    return ''.join(reduce(
        lambda x, y: sorted([x, y])[0],
        allShorts(longN, length))).title()


def blurth(longN):
    return sum([len(allShorts(longN, i)) for i in range(len(longN))])


def main():
    longN = input("Full element name?\n").strip().lower()
    short = input("Short element name?\n").strip().lower()

    print("\n\n")
    if (checkElement(longN, short)):
        print("Short name follows rules")
    else:
        print("Short name does not follow rules")

    print("\nChallange 1:", findShortName(longN))
    print("\nChallange 2:", len(allShorts(longN)))
    print("\nChallange 3:", blurth(longN))


if __name__ == '__main__':
    main()

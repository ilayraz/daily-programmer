# https://www.reddit.com/r/dailyprogrammer/comments/4so25w/20160713_challenge_275_intermediate_splurthian/


def findName(name, nameList):
    for i in range(len(name) - 1):
        for n in range(i + 1, len(name)):
            short = name[i].upper() + name[n]
            if short not in nameList:
                return nameList + [short]
    return None


def main():
    elements = open("ElementList.txt").read().lower().split("\n")
    nameList = list()

    for element in elements:
        nameList = findName(element, nameList)
        if nameList is not None:
            print("%s: %s" % (element, nameList[-1]))
        else:
            print("A short name cannot be found for %s" % element)
            break

if __name__ == '__main__':
    main()

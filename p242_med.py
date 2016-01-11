# https://www.reddit.com/r/dailyprogrammer/comments/3u6o56/
# All functions expect there to be a text file with name 'timetable.txt' in the same directory folder as the script


def normal():
    times = sorted([item.split(' ') for item in open('timetable.txt').read().split("\n")], key=lambda x: x[1])
    current = times[0]
    use = [current]

    for i in times[1:]:
        if current[1] <= i[0]:
            use.append(i)
            current = i

    return len(use)


def bonus1():
    times = sorted([[int(item[:4]), int(item[5:9]), item[10:]] for item in open('timetable.txt').read().split("\n")], key=lambda x: x[1])
    current = times[0]
    use = [current[2]]

    for i in times[1:]:
        if current[1] <= i[0]:
            use.append(i[2])
            current = i

    return "\n".join(use)


def bonus2():
    times = open('timetable.txt').read().split("\n")
    must = times.pop(0)

    times = sorted([[int(item[:4]), int(item[5:9]), item[10:]] for item in times], key=lambda x: x[1])

    current = times.pop([i[2] for i in times].index(must))
    use = [current[2]]

    for i in times[1:]:
        if current[1] <= i[0]:
            use.append(i[2])
            current = i

    return "\n".join(use)

data = [0]
i = 0


def left():
    global i
    if not i:
        raise IndexError('index can\'t be negative')
    i -= 1


def right():
    global i
    i += 1
    if i == len(data):
        data.append(0)

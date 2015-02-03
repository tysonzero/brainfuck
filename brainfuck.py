class Brainfuck(object):
    def __init__(self):
        self.data = [0]
        self.i = 0
        self.code = ''
        self.ci = 0
        self.text = ''
        self.ti = 0

    def right(self):
        self.i += 1
        if self.i == len(self.data):
            self.data.append(0)

    def left(self):
        if not self.i:
            raise IndexError('index can\'t be negative')
        self.i -= 1

    def plus(self):
        self.data[self.i] += 1

    def minus(self):
        self.data[self.i] -= 1

    def output(self):
        print chr(self.data[self.i])

    def input(self):
        self.data[self.i] = ord(self.text[self.ti])
        self.ti += 1

    def next(self):
        if self.code[self.ci] == '>':
            self.right()
        elif self.code[self.ci] == '<':
            self.left()
        elif self.code[self.ci] == '+':
            self.plus()
        elif self.code[self.ci] == '-':
            self.minus()
        elif self.code[self.ci] == '.':
            self.output()
        elif self.code[self.ci] == ',':
            self.input()
        self.ci += 1

    def run(self):
        while self.ci != len(self.code):
            self.next()

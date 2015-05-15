from sys import argv


class Brainfuck(object):
    def __init__(self, code='', text=''):
        self.data = [0]
        self.i = 0
        self.code = code
        self.ci = 0
        self.text = text
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

    def start(self):
        if not self.data[self.i]:
            for i in xrange(self.ci + 1, len(self.code)):
                if self.code[self.ci:i+1].count('[') == self.code[self.ci:i+1].count(']'):
                    self.ci = i
                    return

    def end(self):
        if self.data[self.i]:
            for i in reversed(xrange(1, self.ci)):
                if self.code[i:self.ci+1].count('[') == self.code[i:self.ci+1].count(']'):
                    self.ci = i
                    return

    def debug(self):
        print ' '.join('({})'.format(self.data[i]) if i == self.i else str(self.data[i]) for i in xrange(len(self.data)))

    def next(self):
        {
            '>': self.right,
            '<': self.left,
            '+': self.plus,
            '-': self.minus,
            '.': self.output,
            ',': self.input,
            '[': self.start,
            ']': self.end,
            '#': self.debug,
        }.get(self.code[self.ci], lambda: None)()
        self.ci += 1

    def run(self):
        while self.ci != len(self.code):
            self.next()


if __name__ == '__main__':
    if len(argv) == 1:
        print
        print 'Available Commands:'
        print 'debug [text]'
        print 'run [code] [text]'
        print
    elif argv[1] == 'debug':
        brainfuck = Brainfuck(text=argv[2] if len(argv) > 2 else '')
        while True:
            brainfuck.code += raw_input()
            brainfuck.run()
            brainfuck.debug()
    elif argv[1] == 'run':
        Brainfuck(code=argv[2] if len(argv) > 2 else '', text=argv[3] if len(argv) > 3 else '').run()

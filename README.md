Brainfuck
===============

A Brainfuck interpreter written in Python

Example command line usage:
---------------------------

    python brainfuck.py run ',[>+<-]>.' 'A'

Example python usage:
---------------------

    from brainfuck import Brainfuck
    print Brainfuck(code=',[>+<-]>.', text='A').run()

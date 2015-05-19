Brainfuck
===============

A Brainfuck interpreter written in Python

Instructions
------------

Example command line usage:

    python brainfuck.py run ',[>+<-]>.' 'A'

Example python usage:

    from brainfuck import Brainfuck
    Brainfuck(code=',[>+<-]>.', text='A').run()

#!/usr/bin/env python2.7
# encoding: utf-8

"""
    @brief: 
    @author: icejoywoo
    @date: 15/11/28
"""


def foo():
    while True:
        a = yield
        print a


bar = foo()
# trigger the generator
bar.next()
bar.send('Hello, yield!')
bar.send('Hello, yield!')

bar = foo()
# trigger the generator
bar.send(None)
bar.send('Hello, yield!')
bar.send('Hello, yield!')

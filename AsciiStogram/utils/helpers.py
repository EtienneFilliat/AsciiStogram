#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

isiterable = lambda x: hasattr(x, '__iter__') or hasattr(x, '__getitem__')

def printcolour(text, sameline=True):
    """
    Print color text using escape codes
    """
    if sameline:
        sep = ''
    else:
        sep = '\n'
    sys.stdout.write('\033[97m' + text + '\033[39m' + sep)

def xlab_display(text, width, step, offset=0):
    """
    Display centered x axis label
    """
    print(" " * offset + " " + (text + " - step: " + str(step)).center(width) + " " + "\n")

def print_box_text(text, width, offset=0, spacer=True, bold=True):
    """
    Return text inside an ascii textbox
    """
    box = " " * offset + "-" * (width+2) + "\n"
    if bold:
        box += " " * offset + "|" + '\033[1m' + text.center(width) + '\033[0m' + "|" + "\n"
    else:
        box += " " * offset + "|" + text.center(width) + "|" + "\n"
    box += " " * offset + "-" * (width+2)
    print (box)
    if spacer:
        print()

def get_x_span(data):
    """
    Return the lower and higher value on a list as a tuple
    """
    return min(data), max(data)

def get_y_span(data, x_min, x_max):
    """
    Return the lower and higher value on Y from a list as a tuple
    """
    values = {}
    for i in range(x_min, x_max):
        values[i] = data.count(i)
    return values.get(min(values, key=values.get)),values.get(max(values, key=values.get))

def read_numbers(numbers):
    """
    Read the input data
    """
    for number in numbers:
        yield float(str(number).strip())

def drange(start, stop, step=1.0, include_stop=False):
    """
    Generate between 2 numbers w/ optional step, optionally include upper bound
    """
    if step == 0:
        step = 0.01
    r = start

    if include_stop:
        while r <= stop:
            yield r
            r += step
            r = round(r, 10)
    else:
        while r < stop:
            yield r
            r += step
            r = round(r, 10)

def round_of_rating(number):
    """Round a number to the closest half integer.
    >>> round_of_rating(1.3)
    1.5
    >>> round_of_rating(2.6)
    2.5
    >>> round_of_rating(3.0)
    3.0
    >>> round_of_rating(4.1)
    4.0"""

    return round(number * 2) / 2
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import statistics
import math
from .utils.helpers import *

class Histogram:

    def __init__(self, user_data, x_axis_step=5, pch="X",
                    bincount=None, title=None, xlab=None,
                    showSummary=False):

        if user_data is None or not isiterable(user_data):
            raise Exception("Empty data set !")
        self.data = user_data                                                   # Data List
        self.pch = pch                                                          # Character to create bins in graph
        self.title = title
        self.xlab = xlab                                                        # Graph Title
        self.binwidth = None
        self.showSummary = showSummary                                             # Bins step
        self.x_span = get_x_span(self.data)                                     # X axis lower [0] and higher [1] values
        self.y_span = get_y_span(self.data, self.x_span[0], self.x_span[1])     # Y axis lower [0] and higher [1] values
        if x_axis_step < 2:
            self.x_step = 2
        else:
            self.x_step = int(x_axis_step)
        if bincount is None:
            self.bincount = self.x_span[1] - self.x_span[0]
        else:
            self.bincount = bincount
        self.mean = statistics.mean(self.data)
        self.stderiv = statistics.stdev(self.data)

    def calc_bins(self, n, min_val, max_val):
        """
        Calculate number of bins for the histogram
        """
        if not self.bincount:
            self.bincount = max(10, math.log(n + 1, 2))
        if self.binwidth == 0:
            self.binwidth = 0.1
        if self.binwidth is None:
            self.binwidth = (max_val - min_val) / self.bincount
        for b in drange(float(min_val), float(max_val), step=self.binwidth, include_stop=True):
            if b.is_integer():
                yield int(b)
            else:
                yield b

    def populate_hist(self, bins):
        hist = dict((i, 0) for i in range(len(bins)))
        for number in read_numbers(self.data):
            for i, b in enumerate(bins):
                if number <= b:
                    hist[i] += 1
                    break
            if number == self.x_span[0] and self.x_span[1] > bins[len(bins) - 1]:
                hist[len(hist) - 1] += 1

        return hist

    def display_graph(self, hist, ys, nlen):
        used_labs = set()
        for y in ys:
            ylab = str(int(y))
            if ylab in used_labs:
                   ylab = ""
            else:
                used_labs.add(ylab)
            ylab = " " * (nlen - len(ylab)) + ylab + "|"
            print(ylab, end='')

            for i in range(len(hist)):
                if int(y) <= hist[i]:
                    printcolour(self.pch)
                else:
                    printcolour(" ")
            print('')

    def display_X_abscis(self, nlen, hist):
        bar = " " * (nlen) + "\\"
        x_marks = " " * (nlen + 1)

        i = 0
        inc_step = round_of_rating((self.x_span[1] + 1 - self.x_span[0]) / self.bincount)
        while i <= self.x_span[1] + 1:
            if (i % self.x_step == 0):
                bar += '\033[1m' + "|" + '\033[0m'
                if len(str(int(i))) >= 2:
                    x_marks = x_marks[:-1]
                x_marks += '\033[1m' + str(int(i)) + '\033[0m'
            else:
                x_marks += " "
                bar += "-"
            i += inc_step

        print(bar)
        print(x_marks)
        print()

        if self.xlab:
            xlab_display(self.xlab, max(len(hist), len(self.xlab)), inc_step, nlen)

    def display_summary(self, width, offset=0, spacer=True):
        print_box_text("Summary", width, offset, False)
        summary = " " * offset + "|" + ("observations: %d" % len(self.data)).center(width) + "|\n"
        summary += " " * offset + "|" + ("min value: %f" % self.x_span[0]).center(width) + "|\n"
        summary += " " * offset + "|" + ("mean : %f" % self.mean).center(width) + "|\n"
        summary += " " * offset + "|" + ("std dev : %f" % self.stderiv).center(width) + "|\n"
        summary += " " * offset + "|" + ("max value: %f" % self.x_span[1]).center(width) + "|\n"
        summary += " " * offset + "-" * (2 + width)
        print(summary)
        if spacer:
            print()


    def show(self):
        bins = list(self.calc_bins(len(self.data), self.x_span[0], self.x_span[1]))
        hist = self.populate_hist(bins)

        start = max(self.y_span[0], 1)
        stop = self.y_span[1] + 1
        ys = list(drange(start, stop, float(stop - start) / self.y_span[1])) #self.__height))
        ys.reverse()

        nlen = max(len(str(self.y_span[0])), len(str(self.y_span[1]))) + 1

        if self.title:
            print_box_text(self.title, max(len(hist), len(self.title)), nlen)

        self.display_graph(hist, ys, nlen)
        self.display_X_abscis(nlen, hist)

        if self.showSummary:
            self.display_summary(max(len(hist), len(self.title)), nlen)





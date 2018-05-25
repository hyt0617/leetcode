# !/usr/bin/env python
# -*-coding: utf-8 -*-


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._stack = []
        self._order = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self._stack.append(x)
        self._order.append(x)
        self._order.sort()

    def pop(self):
        """
        :rtype: void
        """
        r = None
        if self._stack:
            r = self._stack[-1]
            self._stack = self._stack[0:len(self._stack) - 1]
            self._order.remove(r)
            self._order.sort()
        return r

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1] if self._stack else None

    def getMin(self):
        """
        :rtype: int
        """
        return self._order[0] if self._order else None


class MinStack1:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min = 2 ** 32 - 1
        self._stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if x <= self._min:
            self._stack.append(self._min)
            self._min = x
        self._stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        peak = self._stack.pop()
        if peak == self._min:
            self._min = self._stack.pop()
        return peak

    def top(self):
        """
        :rtype: int
        """
        return self._stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self._min

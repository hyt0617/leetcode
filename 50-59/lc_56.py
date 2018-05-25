# !/usr/bin/env python
# -*-coding: utf-8 -*-


def merge(intervals):
    """
    :type intervals: List[Interval]
    :rtype: List[Interval]
    """
    inter = sorted(intervals, key=lambda x: x.start)
    merged = []
    start = 0
    while start < len(inter):
        pivot = inter[start]
        j = start + 1
        while j < len(inter) and (pivot.start <= inter[j].start <= pivot.end):
            merged.append(inter[j])
            if inter[j].end >= pivot.end:
                pivot.end = inter[j].end
            j += 1
        start = j
    for m in merged:
        if m in inter:
            inter.remove(m)
    return inter

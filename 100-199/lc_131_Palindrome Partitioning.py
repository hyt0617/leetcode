# !/usr/bin/env python
# -*-coding: utf-8 -*-


def partition(s):
    """
    :type s: str
    :rtype: List[List[str]]
    """

    def search(ps, res, results):
        for i in range(len(ps)):
            current = ps[0:i + 1]
            if current == current[::-1]:
                res.append(current)
                left = ps[i + 1:]
                search(left, res, results)
                t = res[:]
                if not left and t not in results:
                    results.append(t)
                if left and left[::-1] == left:
                    t.append(left)
                    if t not in results:
                        results.append(t)
                res.pop()

    results = []
    search(s, [], results)
    return results

# !/usr/bin/env python
# -*-coding: utf-8 -*-


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    my_dict = {}
    for ele in strs:
        key = sorted(ele)
        group = my_dict.setdefault("".join(key), [])
        group.append(ele)
    return list(my_dict.values())

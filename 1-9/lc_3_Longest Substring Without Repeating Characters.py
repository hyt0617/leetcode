# !/usr/bin/env python
# -*-coding: utf-8 -*-


def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if not s:
        return 0
    used = []
    results = []
    for idx, ele in enumerate(s):
        if ele not in used:
            used.append(ele)
        else:
            if not results or len(used) > len(results[-1]):
                results.append("".join(used))
            idx = used.index(ele)
            used = used[idx + 1:]
            used.append(ele)
    print(results, used)
    if used and (not results or len(used) > len(results[-1])):
        return len("".join(used))
    return len(results[-1])


def lengthOfLongestSubstring_clean(s):
    """
    :type s: str
    :rtype: int
    """
    start = max_length = 0
    used = {}
    for i in range(len(s)):
        if s[i] in used and start <= used[s[i]]:
            start = used[s[i]] + 1
        else:
            max_length = max(max_length, i - start + 1)
        used[s[i]] = i
    return max_length

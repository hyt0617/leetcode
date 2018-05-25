# !/usr/bin/env python
# -*-coding: utf-8 -*-


def wordBreak(s, wordDict):
    """
    :type s: str
    :type wordDict: List[str]
    :rtype: List[str]
    """
    def search(ps, wordDict, mem):
        if ps in mem:
            return mem[ps][:]
        res = []
        if not ps:
            res.append("")
            return res[:]
        for c in wordDict:
            if ps.startswith(c):
                sublist = search(ps[len(c):], wordDict, mem)
                for sub in sublist:
                    r = c + " " + sub if sub else c + sub
                    res.append(r)
        mem[ps] = res[:]
        return res
    return search(s, wordDict, {})


print(wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
, ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
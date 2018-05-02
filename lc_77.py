
def combine(n, k):
    """
    :type n: int
    :type k: int
    :rtype: List[List[int]]
    """
    def combination(nums, r, count, res):
        if count == 0:
            res.append(r[:])
            return
        else:
            i = 0
            while i < len(nums):
                r.append(nums[i])
                combination(nums[i+1:], r, count-1, res)
                r.pop()
                i += 1
    nums = [i for i in range(1, n+1)]
    res = []
    combination(nums, [], k, res)
    return res


print(combine(4, 2))

def permute(nums):
    def backtrack(first):
        if first == n:
            res.append(nums[:])

        for i in range(first, n):
            nums[i], nums[first] = nums[first], nums[i]
            backtrack(first + 1)
            nums[i], nums[first] = nums[first], nums[i]

    n = len(nums)
    res = list()
    backtrack(0)
    return res


a = [1, 2, 3]
print(permute(a))

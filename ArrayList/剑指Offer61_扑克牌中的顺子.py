def isStraight(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    # 排序
    nums.sort()
    # 计算0的数量
    count = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count += 1
        else:
            if i > 0 and nums[i - 1] != 0:
                if nums[i] - nums[i - 1] == 0: return False
                count -= nums[i] - nums[i - 1] - 1
    return False if count < 0 else True


a = [11,0,9,0,0]
isStraight(a)

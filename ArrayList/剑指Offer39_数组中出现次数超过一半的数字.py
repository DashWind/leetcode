def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 1
    temp = nums[0]
    for i in range(1, len(nums)):
        if count == 0:
            temp = nums[i]
        if nums[i] == temp:
            count += 1
        else:
            count -= 1
    return temp


print(majorityElement([1,2,3,2,2,2,5,4,2]))
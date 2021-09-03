# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
# 你可以按任意顺序返回答案。


def two_sum(nums, target):
    """
    给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那两个整数，并返回它们的数组下标。

    你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

    你可以按任意顺序返回答案。

    :param List nums:  整数数组
    :param int target: 目标值
    :return: List[int, int]
    """
    list_map = {}
    for i, num in enumerate(nums):
        if target - num in list_map:
            return [list_map[target - num], i]
        list_map[num] = i
    return []


if __name__ == "__main__":
    # nums = [2, 7, 11, 15], target = 9
    result = two_sum([2, 7, 11, 15], 9)
    print(result)

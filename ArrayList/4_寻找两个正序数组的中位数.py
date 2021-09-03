

def find_median_sorted_arrays(nums1, nums2):
    """
    给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

    合并两个有序数组并找中位数

    :param nums1:
    :param nums2:
    :return:
    """
    nums3 = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] < nums2[j]:
            nums3.append(nums1[i])
            i += 1
        else:
            nums3.append(nums2[j])
            j += 1

    if i == len(nums1):
        while j < len(nums2):
            nums3.append(nums2[j])
            j += 1
    elif j == len(nums2):
        while i < len(nums1):
            nums3.append(nums1[i])
            i += 1

    if (len(nums2) + len(nums1)) % 2 == 0:
        return (nums3[((len(nums2) + len(nums1)) // 2)] + nums3[((len(nums2) + len(nums1)) // 2) - 1]) / 2.0
    else:
        return nums3[(len(nums2) + len(nums1)) // 2]


if __name__ == "__main__":
    nums1, nums2 = [1, 2], [3, 4]
    res = find_median_sorted_arrays(nums1, nums2)
    print(res)

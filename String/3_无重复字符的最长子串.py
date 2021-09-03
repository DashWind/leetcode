

def length_of_longest_substring(s):
    """
    给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度.

    滑动窗口
    向后遍历计算不重复的最长子串
    出现重复则从上一次出现的位置重新计数

    :param string s:
    :return: int
    """
    occ = set()
    max_length = 0
    start = 0
    for i in range(len(s)):
        while s[i] in occ:
            occ.remove(s[start])
            start += 1
        occ.add(s[i])
        curr_length = i - start + 1
        max_length = max(curr_length, max_length)
    return max_length


if __name__ == "__main__":
    ss = "abcabcbb"
    res = length_of_longest_substring(ss)
    print(res)


def is_palindrome(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left, right


def longest_palindrome(s):
    """
    给你一个字符串 s，找到 s 中最长的回文子串。

    中心相同 左右两边相同 为回文子串

    :param s:
    :return:
    """
    if not s:
        return ""

    start, end = 0, 0
    for i in range(len(s)):
        left1, right1 = is_palindrome(s, i, i)
        left2, right2 = is_palindrome(s, i, i + 1)
        if right1 - left1 > end - start:
            start = left1
            end = right1
        if right2 - left2 > end - start:
            start = left2
            end = right2
    return s[start + 1: end]


if __name__ == "__main__":
    ss = "babad"
    res = longest_palindrome(ss)
    print(res)

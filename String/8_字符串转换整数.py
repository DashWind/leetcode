
def myAtoi(s):
    """
    请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）

    :type s: str
    :rtype: int
    """
    num = ""
    for i, ch in enumerate(s):
        if ch != " ":
            num += ch
        if i > 0 and s[i] == ' ' and (0 <= ord(s[i - 1]) - 48 <= 9 or s[i - 1] in ['-', '+']):
            break

    if len(num) > 0 and num[0] not in ['-', '+'] and not (0 <= ord(num[0]) - 48 <= 9):
        return 0

    num2 = ""
    for i, ch in enumerate(num):
        if i == 0 and ch in ['-', '+']:
            num2 += ch
        elif 0 <= ord(ch) - 48 <= 9:
            num2 += ch
        else:
            break

    if len(num2) == 1 and not (0 <= ord(num2[0]) - 48 <= 9):
        return 0

    num2 = int(num2)
    if -2 ** 31 > num2: num2 = -2147483648
    if num2 > 2 ** 31: num2 = 2147483647
    return num2


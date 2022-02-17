def generateParenthesis(n):
    """
    :type n: int
    :rtype: List[str]
    """
    ans = []

    def backtrack(S, left, right):
        if len(S) == 2 * n:
            ans.append("".join(S))
        if left < n:    # 左括号的数量需要小于 总数的一半
            S.append("(")
            backtrack(S, left + 1, right)
            S.pop()
        if right < left:    # 右括号需要小于当前左括号数量 才能添加
            S.append(")")
            backtrack(S, left, right + 1)
            S.pop()

    backtrack([], 0, 0)
    return ans


if __name__ == "__main__":
    generateParenthesis(10)


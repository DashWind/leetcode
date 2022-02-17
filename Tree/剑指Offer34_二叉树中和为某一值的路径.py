



def pathSum(root, target):

    res = list()
    path = list()

    def dfs(root, target):
        if not root: return

        # 前序遍历存放路径
        target -= root.val
        path.append(root.val)
        if not root.left and not root.right and target == 0:
            res.append(path[:])     # 复制路径

        dfs(root.left, target)
        dfs(root.right, target)
        path.pop()

    dfs(root, target)
    return res
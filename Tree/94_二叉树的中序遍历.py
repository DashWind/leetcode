from Tree import TreeUtils


def inorder_traversal(root):
    """
    给定一个二叉树的根节点 root ，返回它的 中序 遍历。

    :param root:
    :return:
    """
    inorder_traversal(root.left)
    print(root.val)
    inorder_traversal(root.right)


if __name__ == "__main__":
    TreeUtils.generate_tree([1, 3, 2, 4, 2, 3, 5])

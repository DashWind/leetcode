class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class TreeUtils:

    @staticmethod
    def generate_tree(nums):
        """
        通过数组生成二叉树

        [1, null, 2, 3]

               1
                \
                 2
                /
               3

        :param nums:
        :return:
        """

        def tree(root, ind):
            if ind >= len(nums) // 2 - 1:
                return
            root.left = TreeNode(nums[2 * ind + 1])
            tree(root.left, ind + 1)
            root.right = TreeNode(nums[2 * ind + 2])
            tree(root.right, ind + 1)

        root = TreeNode(val=nums[0])
        tree(root, 0)
        return root


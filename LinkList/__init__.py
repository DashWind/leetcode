class ListNode:
    """
    链表节点
    """

    def __init__(self, val=0, nt=None):
        self.val = val
        self.next = nt


class LinkList:

    def __init__(self, nums):
        """
        将数组转化为链表 并返回头结点指针

        :param List nums:
        :return: head
        """
        head = ListNode()
        p = head
        for num in nums:
            p.next = ListNode(val=num)
            p = p.next
        self.head = head.next


class LinkListUtils:

    @staticmethod
    def print_link_list(head):
        while head:
            print(head.val)
            head = head.next

from LinkList import ListNode, LinkListUtils
from LinkList import LinkList


def add_two_numbers(l1, l2):
    """
    给你两个非空 的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。

    请你将两个数相加，并以相同形式返回一个表示和的链表。

    你可以假设除了数字 0 之外，这两个数都不会以 0开头。

    :param LinkList l1:
    :param LinkList l2:
    :return: LinkList
    """
    res = ListNode()
    p = res
    # 初始进位 0
    x = 0

    while l1 or l2 or x:
        y = 0
        if l1:
            y += l1.val
            l1 = l1.next
        if l2:
            y += l2.val
            l2 = l2.next

        # 本位上数字为 两个链表对应位置数字相加加上进位 的个位数
        y += x
        x = y // 10 % 10  # 十位
        p.next = ListNode(val=y % 10)  # 个位
        p = p.next
    return res.next


if __name__ == "__main__":
    l1, l2 = LinkList([2, 4, 3]), LinkList([5, 6, 4])
    res = add_two_numbers(l1.head, l2.head)
    LinkListUtils.print_link_list(res)


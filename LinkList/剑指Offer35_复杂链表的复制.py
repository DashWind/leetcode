from LinkList import ListNode


def copy_random_list(head):
    """
    复杂链表的复制
    除了一个next指针指向下一个结点 还加入了一个random指针指向随机结点

    # 1. 将每个结点复制后 放在被复制结点之后 组合成新的链表
    # 2. 将每个结点的random指针复制出来
    # 3. 将链表分割成两个链表

    :param head:
    :return:
    """
    if not head:
        return None

    node = head
    while node:
        node_new = ListNode(val=node.val)
        node_new.next = node.next
        node.next = node_new
        node = node.next.next

    node = head
    while node:
        node_new = node.next
        node_new.random = node.random.next if node.random else None
        node = node.next.next

    head_new = head.next
    node = head
    while node:
        node_new = node.next
        node.next = node.next.next
        node_new.next = node_new.next.next if node_new.next else None
        node = node.next

    return head_new

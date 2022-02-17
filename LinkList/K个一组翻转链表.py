# =========================================================================
# -*- coding: utf-8 -*-
# @Author  :   Neil Zhang
# @Time    :   2022/2/14 13:46
# @Desc    :   每K个结点一组翻转链表 剩余不足K个按原顺序
# =========================================================================
class ListNode:

    def __init(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head, k):
        hair = ListNode(val=0)
        hair.next = head
        pre = hair

        while head:
            tail = pre
            for i in range(k):
                tail = tail.next
                if not tail:
                    return hair.next
            nex = tail.next
            head, tail = self.reverse(head, tail)
            pre.next = head
            tail.next = nex
            pre = tail
            head = tail.next
        return hair.next

    def reverse(self, head, tail):
        prev = tail.next
        p = head
        while prev != tail:
            nex = p.next
            p.next = prev
            prev = p
            p = nex
        return tail, head


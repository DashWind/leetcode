class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def mergeTwoLists(l1, l2):
            if not l1 or not l2:
                return l1 if l1 else l2

            head = ListNode(0)
            tail = head
            while l1 and l2:
                if l1.val > l2.val:
                    tail.next = l2
                    l2 = l2.next
                else:
                    tail.next = l1
                    l1 = l1.next
                tail = tail.next
            tail.next = l1 if l1 else l2
            return head.next

        def merge(lists, l, r):
            if l == r:
                return lists[l]
            if l > r:
                return None
            mid = (l + r) // 2
            return mergeTwoLists(merge(lists, l, mid), merge(lists, mid + 1, r))

        return merge(lists, 0, len(lists) - 1)
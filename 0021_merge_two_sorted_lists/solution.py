class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:
            return None

        if l1 is None:
            return l2

        if l2 is None:
            return l1

        new_list = None
        new_list_cursor = None

        while True:
            if l1 == None or l2 == None:
                break

            node = None
            if l1.val > l2.val:
                node = l2
                l2 = l2.next
            else:
                node = l1
                l1 = l1.next

            if new_list == None:
                new_list = node
                new_list_cursor = new_list
            else:
                new_list_cursor.next = node
                new_list_cursor = new_list_cursor.next

        if l1 == None:
            while not l2 == None:
                new_list_cursor.next = l2
                new_list_cursor = new_list_cursor.next
                l2 = l2.next
        else:
            while not l1 == None:
                new_list_cursor.next = l1
                new_list_cursor = new_list_cursor.next
                l1 = l1.next
        return new_list


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

sol.mergeTwoLists(l1,l2)


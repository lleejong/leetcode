# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cursor = head
        prev_cursor = None
        while cursor is not None:
            if prev_cursor is None:
                prev_cursor = cursor
            elif prev_cursor.val == cursor.val:
                prev_cursor.next = cursor.next
            else:
                prev_cursor = cursor
            cursor = cursor.next
        return head
    def printListNode(self, head: ListNode):
        cursor = head
        while True:
            print(cursor.val, end='')
            cursor = cursor.next
            if cursor is not None:
                print("->", end='')
            else:
                break
        print()


sol = Solution()
l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(2)

sol.printListNode(sol.deleteDuplicates(l1))

l2 = ListNode(1)
l2.next = ListNode(1)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(3)

sol.printListNode(sol.deleteDuplicates(l2))

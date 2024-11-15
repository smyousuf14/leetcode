# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None:
            return head
        prevVal = head
        nextVal = head.next
        print(prevVal)
        print(nextVal)
        
        while nextVal is not None:
            temp = nextVal.next
            nextVal.next = prevVal
            prevVal = nextVal
            nextVal = temp
        head.next = None
        return prevVal
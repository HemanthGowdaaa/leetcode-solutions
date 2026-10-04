# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next or not head.next.next:
            return head
        end = mid = head
        while end.next and end.next.next:
            end = end.next.next
            mid = mid.next
        p2=mid.next
        mid.next=None
        p1 = head
        prev = None
        new = ListNode()
        while p2:
            new.next = p2.next
            p2.next = prev
            prev=p2
            p2 =new.next
        p2 = prev
        while p2:
            p1next = p1.next
            p2next = p2.next 
            p1.next = p2
            p2.next = p1next
            p1=p1next
            p2=p2next



        
        
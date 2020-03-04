# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        odd, even = ListNode(0),  ListNode(0)
        odd_head, even_head = odd, even
        
        is_odd = True
        while head:
            if is_odd:
                odd.next = ListNode(head.val)
                odd = odd.next
            else:
                even.next = ListNode(head.val)
                even = even.next
            
            is_odd = not is_odd
            head = head.next
        
        odd.next = even_head.next
        
        return odd_head.next
        
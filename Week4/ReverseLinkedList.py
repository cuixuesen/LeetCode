# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev, curr = None, head
        
        while curr:
            temp_node = curr.next
            curr.next = prev
            prev = curr
            curr = temp_node
            
        return prev
        
        
        
        
        
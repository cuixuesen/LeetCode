# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        
        k = len(lists)
        mymapping = ["HI"] * k
        
        for i in range(k):
            if lists[i]:
                mymapping[i] = lists[i].val
                lists[i] = lists[i].next
        
        head = None
        
        while mymapping.count("HI") != k:
            curr_min = min(mymapping)
            curr_index = mymapping.index(curr_min)
            if not head:
                head = ListNode(curr_min)
                my_head = head
            else:
                head.next = ListNode(curr_min)
                head = head.next
            
            if lists[curr_index]:   
                mymapping[curr_index] = lists[curr_index].val
                lists[curr_index] = lists[curr_index].next
            else:
                mymapping[curr_index] = "HI"
            
        if head:
            return my_head
        else:
            return None
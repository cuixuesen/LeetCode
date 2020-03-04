# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or head.next is None or m == n:
            return head
        
        if head.next.next is None:
            tmp = head.next
            head.next = None
            tmp.next = head
            return tmp
            

        ctr = 1
        dummy = None
        
        First = False
        
        if m == 1:
            dummy = ListNode(0)
            dummy.next = head
            curr = dummy
            m += 1
            n += 1
            First = True
        else:
            curr = head

        while ctr < m-1 and curr is not None:
            ctr += 1
            curr = curr.next

        mprevNode = curr
        mNode = curr.next
        # M + 1 node
        curr = mNode.next
        ctr += 1
        while ctr < n:
            print(curr.val)
            mNode.next = curr.next
            curr.next = mprevNode.next
            mprevNode.next = curr
            ctr += 1
            curr = mNode.next

        if First:
            return dummy.next

        return head
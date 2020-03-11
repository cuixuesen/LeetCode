"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        
        if not root:
            return []
        
        stack, res = [root], []
        
        while stack:
            curr_node = stack.pop()
            res.append(curr_node.val)
                
            for node in curr_node.children:
                stack.append(node)
        
        return res[::-1]
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.ans = 1
        
        def dfs(curr_node):
            if not curr_node:
                return 0
            
            left = dfs(curr_node.left)
            right = dfs(curr_node.right)
            
            if left and curr_node.val != curr_node.left.val:
                left = 0
            if right and curr_node.val != curr_node.right.val:
                right = 0
                
            self.ans = max(self.ans, left + right + 1)
                    
            return max(left, right) + 1
                    
        dfs(root)
        return self.ans - 1
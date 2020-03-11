# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 1
        def dfs(curr_root):
            
            if not curr_root:
                return 0
            
            left = dfs(curr_root.left)
            right = dfs(curr_root.right)
            self.ans = max(self.ans, left+right+1)
            
            return max(left, right) + 1
        
        dfs(root)
        return self.ans - 1
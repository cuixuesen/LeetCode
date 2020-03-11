# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        curr_node = [root]
        
        while True:
            temp = []
            for node in curr_node:
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
                    
            if not temp:
                break
            else:
                curr_node = temp
            
        return curr_node[0].val
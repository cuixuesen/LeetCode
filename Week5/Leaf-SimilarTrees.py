# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def get_leaf(self,root):
        leaf = ""
        mystack=[]
        mystack.append(root)
        while mystack:
            element = mystack[-1]
            del mystack[-1]
            if element.right != None:
                mystack.append(element.right)
            if element.left != None:
                mystack.append(element.left)
            if element.left == None and element.right == None:
                leaf+=str(element.val)
        return leaf
        
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 == None and root2 == None:
            return True
        leaf1=self.get_leaf(root1)
        leaf2=self.get_leaf(root2)
        
        return leaf1 == leaf2
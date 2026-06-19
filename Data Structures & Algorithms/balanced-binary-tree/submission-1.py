# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function returns height, or -1 if unbalanced
        def check_height(node):
            if not node:
                return 0
            
            # 1. Check left subtree
            left_height = check_height(node.left)
            if left_height == -1: 
                return -1
                
            # 2. Check right subtree
            right_height = check_height(node.right)
            if right_height == -1: 
                return -1
            
            # 3. Check current node balance condition
            if abs(left_height - right_height) > 1:
                return -1
                
            # 4. If balanced, return actual height up to the parent
            return 1 + max(left_height, right_height)
            
        # If the helper doesn't return -1, the tree is balanced
        return check_height(root) != -1
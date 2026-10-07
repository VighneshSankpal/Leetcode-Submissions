# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        curr = root
        while curr:
            if curr.left:
                # Find the rightmost node in the left subtree
                prev = curr.left
                while prev.right:
                    prev = prev.right
                
                # Rewire the right subtree to the right of the rightmost node
                prev.right = curr.right
                
                # Move the left subtree to the right side
                curr.right = curr.left
                curr.left = None
            
            # Move to the next node along the right chain
            curr = curr.right

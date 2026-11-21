# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        
        def num_series(root, order):

            curr_order = order * 10 + root.val
            left_num = 0
            right_num = 0


            if root.left == None and root.right == None:
                return curr_order

            if root.left:
                left_num = num_series(root.left, curr_order)

            if root.right:
                right_num = num_series(root.right, curr_order)

            
            return left_num + right_num

        return num_series(root, 0)
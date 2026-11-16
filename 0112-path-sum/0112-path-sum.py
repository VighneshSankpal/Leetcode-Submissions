# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        
        def is_sum_equal(root,target, curr=0):

            if root == None:
                return False

            curr += root.val

            if root.left == None and root.right == None:
                if target == curr:
                    return True

            
            if is_sum_equal(root.left,target,curr) or is_sum_equal(root.right,target,curr):
                return True
            
            

            return False

        
        return is_sum_equal(root,targetSum,0)
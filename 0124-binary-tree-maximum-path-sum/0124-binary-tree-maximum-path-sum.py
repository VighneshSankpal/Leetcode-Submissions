# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:

        res = [root.val]

        def find_max(root:TreeNode):
            if root == None:
                return 0

            leftside = find_max(root.left)

            rightside  = find_max(root.right)

            leftside = max(leftside,0)
            rightside = max(rightside,0)

            res[0] = max(res[0], leftside+rightside+root.val)

            return root.val + max(leftside,rightside)

        find_max(root)
        return res[0]
        
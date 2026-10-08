# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
        

        my_list = [root.val]

        my_list.extend(self.preorderTraversal(root.left))
        my_list.extend(self.preorderTraversal(root.right))

        return my_list



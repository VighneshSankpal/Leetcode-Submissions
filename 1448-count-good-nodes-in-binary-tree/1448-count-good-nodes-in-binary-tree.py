# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def get_goodnodes(node:TreeNode,max_num)->int:


            if node == None:
                return 0
            
                
            is_goodnode = 0

            
            if node.val >= max_num:
                max_num = node.val
                is_goodnode= 1


            left_node = get_goodnodes(node.left,max_num)
            right_node = get_goodnodes(node.right,max_num)
        
            
            return  is_goodnode + left_node+right_node
        
        return get_goodnodes(root,root.val)
                
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow =  head
        unique_node = list()
        while slow != None:
            if slow in unique_node:
                return slow
            else:
                unique_node.append(slow)

            slow = slow.next
            
        return None    


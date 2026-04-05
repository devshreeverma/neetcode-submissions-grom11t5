# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        first = head
        visited = []

        while first is not None:
            if first in visited:
                return True
            
            visited.append(first)
            first = first.next
        
        return False

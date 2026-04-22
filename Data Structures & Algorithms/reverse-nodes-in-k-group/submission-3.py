# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       prev=None
       first=head
       temp=head
       i=1
       j=0
       while temp is not None and j<k:
         temp=temp.next
         j+=1
       if j<k:
            return head
       while i<=k:
          second=first.next
          first.next=prev
          prev=first
          first=second
          i+=1
          
         
       head.next= self.reverseKGroup(first, k)
       return prev

       
      

               # Check if at least k nodes exist
                   
                       
                              
                                           
                                                   

                                                       # Reverse first k nodes
                                                          
                                                               
                                                                 
                                                                           
                                                                                   
                                                                                           
                                                                                                   
                                                                                                           

                                                                                                         # Recursively reverse next groups
                                                                                                                   
                                                                                                                           

                                                                                                                               

      

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        head1 = l1
        head2 = l2
        
        ans = ListNode(0)
        l3 = ans
        
        carry = 0
        
        while head1 is not None or head2 is not None or carry != 0:
            
            v1 = head1.val if head1 else 0
            v2 = head2.val if head2 else 0
            
            total = v1 + v2 + carry
            
            carry = total // 10
            digit = total % 10
            
            ans.next = ListNode(digit)
            ans = ans.next
            
            if head1:
                head1 = head1.next
            
            if head2:
                head2 = head2.next
        
        return l3.next


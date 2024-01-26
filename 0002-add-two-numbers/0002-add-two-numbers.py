# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
        def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            dummy_head = ListNode()
            current = dummy_head
            carry = 0
                     
        
            while l1 or l2 or carry:
    # Get the values at the current nodes (or 0 if the node is None)

                v1 = l1.val if l1 else 0
                v2 = l2.val if l2 else 0
    
    # Calculate the sum and carry
                sum = v1 + v2 + carry
                carry = sum // 10
            
    # Update the current node with the remainder (the new value)
                current.next = ListNode(sum % 10)
                current = current.next
                 
    # Move to the next nodes if they exist
                if l1:
                    l1 = l1.next
                if l2:
                    l2 = l2.next
                      
            return dummy_head.next
                
                      
        
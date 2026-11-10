# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        int_1 = 0
        int_2 = 0
        carry = 0

        dummy = ListNode()
        node = dummy
        

        while l1 and l2:
            value = carry + l1.val + l2.val
            node_val = value  % 10
            carry = value // 10
            new_node = ListNode(node_val)
            node.next = new_node
            node = new_node
            l1 = l1.next
            l2 = l2.next
        while l1:
            value = carry + l1.val
            node_val = value  % 10
            carry = value // 10
            new_node = ListNode(node_val)
            node.next = new_node
            node = new_node
            l1 = l1.next
        
        while l2:
            value = carry + l2.val
            node_val = value  % 10
            carry = value // 10
            new_node = ListNode(node_val)
            node.next = new_node
            node = new_node
            l2 = l2.next
        if carry:
            new_node = ListNode(carry)
            node.next = new_node
            node = new_node
        
        
        return dummy.next
            

            
            
          
        
        
        

    
            
        
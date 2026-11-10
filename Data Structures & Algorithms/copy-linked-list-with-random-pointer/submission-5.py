"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        node = head

        table = {}

        while node:
            copy_node = Node(node.val)
            table[node] = copy_node
            node = node.next
        node = head

        while node:
            copy_node = table[node]
            if node.random:
                copy_node.random = table[node.random]
            if node.next:
                copy_node.next = table[node.next]
            node = node.next
        return table[head]

        




        

        


    
            
        


        
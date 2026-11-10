class LRUCache:

    class Node:
        def __init__(self, key, val):
            self.val = val
            self.key = key
            self.next = None
            self.prev = None
        

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count  = 0
        self.table = {}
        self.head = self.Node(-1,-1)
        self.tail = self.Node(-1,-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node):
        temp_prev = node.prev
        temp_next = node.next
        node.prev = None
        node.next = None
        temp_prev.next = temp_next
        temp_next.prev = temp_prev

    def _add_to_tail(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node   

    
    

    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self._remove_node(node)
            self._add_to_tail(node)
            return node.val
        return -1
         
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self._remove_node(self.table[key])
        node = self.Node(key,value)
        self._add_to_tail(node)
        self.table[key] = node

        if len(self.table) > self.capacity:
            lru_node = self.head.next
            self._remove_node(lru_node)
            del self.table[lru_node.key]

   
            
            
                
            


            

       


        

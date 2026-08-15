class MinStack:

    def __init__(self):
        self.array = []
        self.length = 0
        self.stack= []
        
        

    def push(self, val: int) -> None:
        self.array.append(val)
        self.stack.append(min(val, self.stack[-1] if self.stack else 100000000000))
        self.length += 1

        

    def pop(self) -> None:
        self.array.pop()
        self.stack.pop()
        self.length -= 1
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.stack[-1]

        

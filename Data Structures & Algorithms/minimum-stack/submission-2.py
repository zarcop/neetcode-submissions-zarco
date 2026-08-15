class MinStack:

    def __init__(self):
        self.array = []
        self.length = 0
        
        

    def push(self, val: int) -> None:
        self.array.append(val)
        self.length += 1
        

    def pop(self) -> None:
        self.array.pop()
        self.length -= 1
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        minElement = 10000000000000
        for i in range(len(self.array)):
            if self.array[i] < minElement:
                minElement = self.array[i]
        return minElement

        

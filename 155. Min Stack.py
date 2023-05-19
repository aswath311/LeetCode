class MinStack:
    
    def __init__(self):
        self.stack = []
        self.min = []
        return
                
    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            self.min.append(val)
        elif val < self.min[-1]:
            self.min.append(val)
        else:
            self.min.append(self.min[-1])
        self.stack.append(val)
        return

    def pop(self) -> None:
        self.min.pop()
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min[-1]
    
m = MinStack()
m.push(-2)
m.push(0)
m.push(-1)
print(m.getMin())
print(m.top())
print(m.pop())
print(m.getMin())

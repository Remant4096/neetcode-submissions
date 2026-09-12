class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:

        if(not self.stack):
            self.min_stack.append(val)
        elif val< self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
        self.stack.append(val)
        return None
        

    def pop(self) -> None:
        if (not self.stack):
            return None
        self.min_stack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_stack[-1]
        
        

        

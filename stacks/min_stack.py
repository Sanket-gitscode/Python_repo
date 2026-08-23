class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minstack = []
    
    def push(self,value):
        self.stack.append(value)
        
        if not self.minstack:
            self.minstack.append(value)
        else:
            self.minstack.append(min(value,self.minstack[-1]))
        
    def pop(self):
        self.stack.pop()
        self.minstack.pop()
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.minstack[-1]
    
S1 = MinStack()
S1.push(1)
S1.push(2)
S1.push(3)
S1.push(4)
print(S1.stack)
S1.pop()
print(S1.top())
print(S1.getMin())
print(S1.stack)

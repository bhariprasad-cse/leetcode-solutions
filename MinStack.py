# LeetCode 155 - Min Stack
# Difficulty: Medium
# Topic: Stack

class MinStack:
    min_values = []
    def __init__(self, minstack):
        self.minstack = minstack

    def push(self, value: int) -> None:
        self.minstack.append(value)
        min_values.append(value)
    
    def pop(self) -> None:
        self.minstack.pop()

    def top(self) -> int:
        return self.minstack[-1]

    def getMin(self) -> int:
        return self.min_value

minStack = MinStack([])
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
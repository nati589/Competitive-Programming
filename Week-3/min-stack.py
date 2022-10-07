class MinStack:

    def __init__(self):
        self.container = []
        self.value = []

    def push(self, val: int) -> None:
        if len(self.container) == 0:
            self.container.insert(0, val)
            self.value.insert(0, val)
        elif val <= self.value[0]:
            self.value.insert(0, val)
            self.container.insert(0, val)
        else:
            self.container.insert(0, val)

    def pop(self) -> None:
        if self.container[0] == self.value[0]:
            self.value.pop(0)
        self.container.pop(0)

    def top(self) -> int:
        return self.container[0]

    def getMin(self) -> int:
        return self.value[0]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

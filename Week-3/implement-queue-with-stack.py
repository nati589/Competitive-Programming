class MyQueue:

    def __init__(self):
        self.container1 = []
        self.container2 = []

    def push(self, x: int) -> None:
        for item in self.container1:
            self.container2.insert(0, item)
        self.container1 = []
        self.container1.append(x)
        for item in self.container2:
            self.container1.insert(0, item)
        self.container2 = []

    def pop(self) -> int:
        return self.container1.pop(0)

    def peek(self) -> int:
        return self.container1[0]

    def empty(self) -> bool:
        return len(self.container1) == 0

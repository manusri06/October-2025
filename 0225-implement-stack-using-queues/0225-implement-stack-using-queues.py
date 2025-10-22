class MyStack:

    def __init__(self):
        self.st1 = deque()
        self.st2 = deque() 

    def push(self, x: int) -> None:
        self.st1.append(x)

        while self.st2:
            self.st1.append(self.st2.popleft())

        self.st1,self.st2 = self.st2,self.st1

    def pop(self) -> int:
        return self.st2.popleft()

    def top(self) -> int:
        return self.st2[0]

    def empty(self) -> bool:
        return len(self.st2) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
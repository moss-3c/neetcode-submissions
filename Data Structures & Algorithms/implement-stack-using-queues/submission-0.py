import queue

class MyStack:

    def __init__(self):
        self.q = queue.LifoQueue()

    def push(self, x: int) -> None:
        self.q.put(x)

    def pop(self) -> int:
        return self.q.get()

    def top(self) -> int:
        num = self.q.get()
        self.q.put(num)
        return num        

    def empty(self) -> bool:
        return self.q.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# -*- coding: utf-8 -*-
# @Time    : 2020/10/8 22:40

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # 3, 2, 5
        self.data = []
        # 1, 0, 2
        self.index = []

    def push(self, x: int) -> None:
        self.data.append(x)
        if not self.index:
            self.index.append(0)
            return
        if x >= self.data[self.index[-1]]:
            self.index.append(len(self.data) - 1)
            return
        for i, idx in enumerate(self.index):
            if x < self.data[idx]:
                self.index = self.index[:i] + [len(self.data) - 1] + self.index[i:]
                break
        print(self.data, self.index)
        return

    def pop(self) -> None:
        self.data.pop()
        self.index.remove(len(self.data))
        return

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.data[self.index[0]]

# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(85);
minStack.push(-99);
minStack.push(67);
# minStack.push(512);
print(minStack.getMin())
minStack.pop()
print(minStack.getMin());  # --> 返回 -3.
minStack.pop()
print(minStack.getMin());  # --> 返回 -3.
minStack.pop();
print(minStack.getMin());  # --> 返回 -2.


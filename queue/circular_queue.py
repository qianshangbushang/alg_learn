# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 22:22
"""
设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。它也被称为“环形缓冲器”。

循环队列的一个好处是我们可以利用这个队列之前用过的空间。在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。但是使用循环队列，我们能使用这些空间去存储新的值。

你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/queue-stack/kzlb5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.head = -1
        self.tail = -1
        self.len = k
        self.data = [0] * k
        return

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        如果队列满了，无法插入
        如果队列空，头指针 + 1， 尾指针+1检查是否越界
        如果队列不为空，尾指针+1检查是否越界
        """
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = 0
        self.tail = (self.tail + 1) % self.len
        self.data[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        如果对列为空 返回False
        如果头指针和尾指针指向同一元素，当前队列只有一个元素，指针都置-1
        如果头指针和尾指针不指向同一个元素，头指针+1 注意是否越界，调整指针位置
        """
        if self.isEmpty():
            return False
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return True
        self.head = (self.head + 1) % self.len
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        if self.isEmpty():
            return -1
        return self.data[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        头指针指向-1时 为空队列
        """
        return self.head == -1

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        头指针和尾指针相差一轮时，表示时满队列
        """
        return ((self.tail + 1) % self.len) == self.head


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(6)
print(obj.enQueue(6)) #[6]
print(obj.Rear())     #[6]
print(obj.Rear())     #[6]
print(obj.deQueue())  #[]
print(obj.enQueue(5)) #[5]
print(obj.Rear())     #[5]
print(obj.deQueue(), obj.head, obj.tail)  #[]
print(obj.Front())    #-1
print(obj.deQueue())  #False
print(obj.deQueue())
print(obj.deQueue())

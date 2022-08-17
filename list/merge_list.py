import heapq
from typing import List


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        return

class NodeHeap:
    def __init__(self, node_list:List[ListNode]):
        self.node_list = node_list
        self.init()
        return

    def pop(self):
        node = self.node_list[0]
        self.node_list[0] = self.node_list[0].next
        if not self.node_list[0]:
            self.node_list = self.node_list[1:]
            self.init()
        else:
            self.node_list[0], self.node_list[-1] = self.node_list[-1], self.node_list[0]
            self.update_heap(0, len(self.node_list))
        return node

    def init(self):
        n = len(self.node_list)
        for i in range(n // 2 - 1, -1, -1):
            self.update_heap(i, n)
        return

    def update_heap(self, i, end):
        j = 2 * i + 1
        while j < end:
            if j + 1 < end and self.node_list[j].val > self.node_list[j+1].val:
                j = j + 1
            if self.node_list[i].val > self.node_list[j].val:
                self.node_list[i], self.node_list[j] = self.node_list[j], self.node_list[i]
                i = j 
                j = 2 * j + 1
            else:
                break
        return

    def is_empty(self):
        return len(self.node_list) == 0



def merge_k_list(node_list:List[ListNode]):
    heap = NodeHeap(node_list)
    dummy = ListNode(-1, None)
    pre = dummy
    while not heap.is_empty():
        node = heap.pop()
        pre.next = node
        pre = pre.next
    return  dummy.next


def merge_list(list1: ListNode, list2: ListNode):
    if not (list1 and list2):
        return list1 if list1 else list2
    if list1.val > list2.val:
        list2.next = merge_list(list1, list2.next)
        return list2
    else:
        list1.next = merge_list(list1.next, list2)
        return list1


def create_list(nums: List[int]):
    dummy = ListNode(-1, None)
    pre = dummy

    for x in nums:
        pre.next = ListNode(x, None)
        pre = pre.next
    return dummy.next


def show_list(node: ListNode):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    print(result)
    return


if __name__ == "__main__":
    list1 = create_list([1, 3, 5, 7, 9])
    list2 = create_list([2, 4, 6, 8, 10])
    list3 = create_list([2, 4, 6, 8, 10])
    # show_list(merge_list(list1, list2))

    show_list(merge_k_list([list1, list2, list3]))

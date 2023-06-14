
class SNode:
    def __init__(self, element=None, next=None) -> None:
        self.element = element
        self.next = next
        return


class LRUBaseLinkList:
    def __init__(self, length:int) -> None:
        self.max_length = length
        self.cur_length = 0
        self.head = SNode()
        return
    
    def add(self, data):
        pre_node = self.find_pre_node(data)

        if pre_node:
            self.delete_node(pre_node)
        else:
            if self.cur_length >= self.max_length:
                self.delete_end()
        self.insert_begin(data)
        return
    
    def find_pre_node(self, data):
        node = self.head
        while node.next:
            if data == node.next.element:
                return node
            node = node.next
        return None

    def delete_node(self, pre_node:SNode):
        temp = pre_node.next
        pre_node.next = temp.next
        temp = None
        self.cur_length -= 1
        return
    
    def delete_end(self):
        node = self.head
        if node.next == None:
            return
        while node.next.next:
            node = node.next
        
        node.next = None
        self.cur_length -= 1
        return

    def insert_begin(self, data):
        temp = self.head.next
        self.head.next = SNode(data, temp)
        self.cur_length += 1
        return
    
    def show(self):
        node = self.head
        print("当前链表中数据：", end='')
        while node.next:
            node = node.next
            print(node.element, end=',')
        print()
    
if __name__ == "__main__":
    l = LRUBaseLinkList(3)

    while True:
        x = input("请输入数据：")
        l.add(x)
        l.show()
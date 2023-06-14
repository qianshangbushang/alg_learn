
class SNode:
    def __init__(self, key=None, val=None) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        return


class LRUCache:
    def __init__(self, cap:int) -> None:
        self.cap = cap
        self.len = 0

        self.node_dict = {}

        self.head = SNode()
        self.tail = SNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        return
    
    def remove_node(self, node:SNode):
        node.prev.next = node.next
        node.next.prev = node.prev
        return
    
    def add_node_last(self, node:SNode):
        node.prev = self.tail.prev
        node.next = self.tail

        self.tail.prev.next = node
        self.tail.prev = node
        return
    
    def move_node_last(self, node:SNode):
        self.remove_node(node)
        self.add_node_last(node)
        return
    
    def get(self, key):
        if key in self.node_dict:
            return self.node_dict[key].val
        return -1

    def put(self, key:int, val:int):
        if key in self.node_dict:
            node = self.node_dict[key]
            node.val = val
            self.move_node_last(node)
            return
        
        if len(self.node_dict) == self.cap:
            del self.node_dict[self.head.next.key]
            self.remove_node(self.head.next)

        node = SNode(key, val)
        self.node_dict[key] = node
        self.add_node_last(node) 
        return
    

    def show(self):
        print("当前链表结构：", end="")
        node = self.tail
        while True:
            if node.prev == self.head:
                break
            node = node.prev
            print(node.val, end=",")
        print()
        return
   
if __name__ == "__main__":
    l = LRUCache(3)

    while True:
        x = input("请输入数据：")
        l.put(x, x)
        l.show()

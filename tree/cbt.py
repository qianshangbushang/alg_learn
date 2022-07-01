class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
    1
  2   3
4   5   6

"""


class CBTInserter:
    def __init__(self, root: TreeNode):
        self.root = root
        self.queue = []
        self.bfs([root])
        return

    def bfs(self, node_list):
        if len(node_list) == 0:
            return
        next_list = []
        for node in node_list:
            self.queue.append(node)
            if node.left:
                next_list.append(node.left)
            if node.right:
                next_list.append(node.right)
        self.bfs(next_list)

    def insert(self, v: int) -> int:
        # 0 -> [1, 2] 2i + 1， 2i+ 2
        # 1 -> [3, 4]
        node = TreeNode(v)
        self.queue.append(node)
        # 0 1 2 3 4
        # 1 -> 2 -> 0, 2 -> 3 -> 0
        # 3 -> 4 -> 1, 4 -> 5 -> 1
        p_node = self.queue[len(self.queue) // 2 - 1]
        if len(self.queue) % 2 == 0:
            p_node.left = node
        else:
            p_node.right = node
        return p_node.val

    def get_root(self) -> TreeNode:
        return self.root

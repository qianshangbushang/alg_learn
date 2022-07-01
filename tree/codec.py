from doctest import REPORT_UDIFF
from socket import SOL_UDP
from tkinter.messagebox import NO
from turtle import right


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root:TreeNode):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "None"

        left_s = self.serialize(root.left)
        right_s = self.serialize(root.right)
        return ",".join([str(root.val), left_s, right_s])
    

    def deserialize(self, data:str):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        order = data.split(",")

        def _des():
            while order:
                x = order.pop(0)
                if x == "None":
                    return None
                node = TreeNode(int(x))
                node.left = _des()
                node.right = _des()
                return node
                
        return _des()


if __name__ == "__main__":

    root = TreeNode(4)
    left_node = TreeNode(3)
    right_node = TreeNode(2)
    root.left = left_node
    root.right = right_node

    left_node.left = TreeNode(1)
    right_node.right = TreeNode(0)
    right_node.left = TreeNode(7)

    s = Codec()
    r =  s.serialize(root)
    print(r)
    s.deserialize(r)


    #    3 
    #  2   4
    #3

    # pre: 3,2,3,4
    # mix: 3,2,3,4
    # 3
    # 3,2,  2,3 / [], []    
    # 4    4/ [2, 3, 4], [2, 3, 4]

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        result = -1
        queue = [root]
        while len(queue) > 0:
            result = queue[0].val
            for _ in range(0, len(queue)):
                x = queue.pop(0)
                if x.left:
                    queue.append(x.left)
                if x.right:
                    queue.append(x.right)
        return result

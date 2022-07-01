
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result = []
        q  = []
        q.append(root)
        while len(q) > 0:
            level_result = []
            for _ in range(len(q)):
                x = q.pop(0)
                # print("x": x)
                level_result.append(x.val)
                if x.left:
                    q.append(x.left)
                if x.right:
                    q.append(x.right)
            result.append(level_result)
        return result
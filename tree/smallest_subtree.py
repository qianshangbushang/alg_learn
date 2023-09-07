# 给定一个根为 root 的二叉树，每个节点的深度是 该节点到根的最短距离 。
# 返回包含原始树中所有 最深节点 的 最小子树 。
# 如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。
# 一个节点的 子树 是该节点加上它的所有后代的集合。

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def traversal(node: TreeNode, depth: int):
            if not node.left and not node.right:
                return node, depth

            left_node, left_depth = None, -1
            right_node, right_depth = None, -1
            if node.left:
                left_node, left_depth = traversal(node.left, depth+1)
            if node.right:
                right_node, right_depth = traversal(node.right, depth+1)
            if left_depth > right_depth:
                return left_node, left_depth
            if left_depth < right_depth:
                return right_node, right_depth
            return node, left_depth

        node, _ = traversal(root, 0)
        return  node

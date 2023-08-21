"""
给你一个有n个节点的 有向无环图(DAG),请你找出所有从节点 0到节点 n-1的路径并输出(不要求按特定顺序)
graph[i]是一个从节点 i 可以访问的所有节点的列表（即从节点 i 到节点graph[i][j]存在一条有向边）。


输入: graph = [[1,2],[3],[3],[]]
输出：[[0,1,3],[0,2,3]]
解释：有两条路径 0 -> 1 -> 3 和 0 -> 2 -> 3


"""
from typing import List
import copy

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        result = []

        def backtrack(curr_node:int, path:List[int]):
            if curr_node == len(graph)  - 1:
                result.append(copy.deepcopy(path))

            for n in graph[curr_node]:
                path.append(n)
                backtrack(n, path)
                path.pop()
            return
        
        backtrack(0, [0])
        return result
    


if __name__ == "__main__":
    s = Solution()
    print(s.allPathsSourceTarget([[1,2],[3],[3],[]]))




# -*- coding: utf-8 -*-
# @Time    : 2020/9/23 23:06

"""
你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

示例：
给定二维网格：
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
运行完你的函数后，该网格应该变成：
 3  -1   0   1
 2   2   1  -1
 1  -1   2  -1
 0  -1   3   4

"""
import math
from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        if not rooms or len(rooms) == 0:
            return
        self.row = len(rooms)
        self.col = len(rooms[0])

        for i in range(self.row):
            for j in range(self.col):
                #  从门向空间搜索
                if rooms[i][j] == 0:
                    self.bfs(rooms, i, j, 0)

    def bfs(self, rooms: List[List[int]], i: int, j: int, val: int, ):
        if i < 0 or j < 0 or i >= self.row or j >= self.col:
            return
        if rooms[i][j] < val:
            return
        rooms[i][j] = val

        self.bfs(rooms, i + 1, j, val + 1)
        self.bfs(rooms, i, j + 1, val + 1)
        self.bfs(rooms, i - 1, j, val + 1)
        self.bfs(rooms, i, j - 1, val + 1)


def showData(data):
    for x in data:
        print(x)
    return


s = Solution()
INF = math.inf
data = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]

]

showData(data)
print("-" * 50)
s.wallsAndGates(data)
showData(data)

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :n_province.py
# @Time      :2023/2/1 9:22


from typing import List

"""
有 n 个城市，其中一些彼此相连，另一些没有相连。如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。

输入：isConnected = [[1,1,0],[1,1,0],[0,0,1]]
输出：2
"""


class Recorder:
    def __init__(self):
        self.f_dict = {}
        return

    def find(self, x):
        if self.f_dict[x] == x:
            return x
        return self.find(self.f_dict[x])

    def merge(self, x, y):
        self.f_dict[self.find(y)] = self.find(x)
        return


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        r = Recorder()

        for i in range(len(isConnected)):
            r.f_dict[i] = i

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if isConnected[i][j] == 1 and i != j:
                    r.merge(i, j)
        cnt = 0
        for k, v in r.f_dict.items():
            if k == v:
                cnt += 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))

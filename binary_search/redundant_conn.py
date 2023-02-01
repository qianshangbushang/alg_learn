#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :redundant_conn.py
# @Time      :2023/2/1 9:35


from typing import List

"""
树可以看成是一个连通且 无环 的 无向 图。
给定往一棵 n 个节点 (节点值 1～n) 的树中添加一条边后的图。添加的边的两个顶点包含在 1 到 n 中间，且这条附加的边不属于树中已存在的边。
图的信息记录于长度为 n 的二维数组 edges ，edges[i] = [ai, bi] 表示图中在 ai 和 bi 之间存在一条边。
请找出一条可以删去的边，删除后可使得剩余部分是一个有着 n 个节点的树。如果有多个答案，则返回数组 edges 中最后出现的边。
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
        self.f_dict[self.find(x)] = self.find(y)
        return


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        r = Recorder()
        max_id = max(max(i) for i in edges)
        for i in range(1, max_id + 1):
            r.f_dict[i] = i
        for e in edges:
            if r.find(e[0]) == r.find(e[1]):
                result = e
            else:
                r.merge(e[0], e[1])
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))

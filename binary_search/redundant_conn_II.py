#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :redundant_conn_II.py
# @Time      :2023/2/1 10:00


from typing import List

"""
在本问题中，有根树指满足以下条件的 有向 图。该树只有一个根节点，所有其他节点都是该根节点的后继。该树除了根节点之外的每一个节点都有且只有一个父节点，而根节点没有父节点。
输入一个有向图，该图由一个有着 n 个节点（节点值不重复，从 1 到 n）的树及一条附加的有向边构成。附加的边包含在 1 到 n 中的两个不同顶点间，这条附加的边不属于树中已存在的边。
结果图是一个以边组成的二维数组 edges 。 每个元素是一对 [ui, vi]，用以表示 有向 图中连接顶点 ui 和顶点 vi 的边，其中 ui 是 vi 的一个父节点。
返回一条能删除的边，使得剩下的图是有 n 个节点的有根树。若有多个答案，返回最后出现在给定二维数组的答案。

"""
"""
先成环，但还没有节点入度为2，成环时我们将第一个使得环出现的边记录下来 这种情况下有两个可能： 
    1. 到最后也没有入度为2的点，这时把先前记录的最后一个使得环出现的边输出 
    2. 有某条边的加入使得某个点入度为2了，那么把第一个指向这个点的边输出， 因为在当前边加入前就已经成环了，则一定是之前那条边使得环出现的。
先出现了入度为2的点，还没有成环，这时 先不union 第二条指向该点的边 这种情况下也有两个可能： 
    1. 最终也没成环，则直接将使得该点入度为2的那条边输出，因为必然是后一条边会导致成环 
    2. 后来成环了，那必然是前一条边导致的成环，因为第二条边的union还没作用呢。
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
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        max_id = max([max(i) for i in edges])
        r = Recorder()
        direct_p, conflict, circle = {}, None, None
        for i in range(1, max_id + 1):
            r.f_dict[i] = i
            direct_p[i] = i

        for e in edges:
            # 先有冲突，当前边导致成环， 删除冲突时先加入的边
            if conflict and r.find(e[0]) == r.find(e[1]):
                return conflict[0]
            # 先成环，当前导致冲突，删除当前子节点的成环边
            if circle and direct_p[e[1]] != e[1]:
                return [direct_p[e[1]], e[1]]
            # 成环，正常记录,并加入并查集
            if r.find(e[0]) == r.find(e[1]):
                circle = e
                r.f_dict[r.find(e[0])] = r.find(e[1])
                direct_p[e[1]] = e[0]
                continue
            # 冲突, 记录先加入的边，不加入并查集
            if direct_p[e[1]] != e[1]:
                conflict = [[direct_p[e[1]], e[1]], e]
                continue
            r.f_dict[r.find(e[0])] = r.find(e[1])
            direct_p[e[1]] = e[0]

        # 冲突，未能成环
        if conflict:
            return conflict[1]
        # 成环，不冲突
        if circle:
            return circle


if __name__ == '__main__':
    s = Solution()
    print(s.findRedundantDirectedConnection([[1, 2], [1, 3], [2, 3]]))
    print(s.findRedundantDirectedConnection([[2, 1], [3, 1], [4, 2], [1, 4]]))

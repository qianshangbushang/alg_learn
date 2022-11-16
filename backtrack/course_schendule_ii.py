#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :course_schendule_ii.py
# @Time      :2022/11/15 17:24
from collections import deque
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}  # collections.defaultdict(list)
        ind = {i: 0 for i in range(numCourses)}  # collections.defaultdict(int)
        for pair in prerequisites:
            adj[pair[1]].append(pair[0])
            ind[pair[0]] += 1
            ind[pair[1]] += 0

        que = deque()
        for i, v in ind.items():
            if v == 0:
                que.append(i)
        visited = []
        while len(que) > 0:
            curr = que.popleft()
            if curr in visited:
                break
            visited.append(curr)
            for nxt in adj[curr]:
                ind[nxt] -= 1
                if ind[nxt] == 0:
                    que.append(nxt)
        if len(visited) == len(ind):
            return visited
        return []


if __name__ == '__main__':
    s = Solution()
    print(s.findOrder(2, [[1, 0]]))
    print(s.findOrder(4, [[1, 0], [2, 0], [3, 1]]))
    print(s.findOrder(1, []))

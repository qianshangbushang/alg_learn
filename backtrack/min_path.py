#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :min_path.py
# @Time      :2022/10/26 14:27


from collections import deque
from typing import List


def logic(matrix: List[List[int]], k: int):
    m, n = len(matrix), len(matrix[0])
    if m == 1 and n == 1:
        return 0

    k = min(k, m + n - 3)
    existed = {(0, 0, k)}
    q = deque([(0, 0, k)])

    step = 0
    while len(q) > 0:
        step += 1
        count = len(q)
        for _ in range(count):
            x, y, k = q.popleft()
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    if matrix[nx][ny] == 0 and (nx, ny, k) not in existed:
                        if nx == m - 1 and ny == n - 1:
                            return step
                        q.append((nx, ny, k))
                        existed.add((nx, ny, k))
                    elif matrix[nx][ny] == 1 and k > 0 and (nx, ny, k - 1) not in existed:
                        q.append((nx, ny, k - 1))
                        existed.add((nx, ny, k - 1))
    return -1

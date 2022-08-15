#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :spiral_order.py
# @Time      :2022/8/12 11:58


from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    result = []
    num = 0
    while num < len(matrix) * len(matrix[0]):
        for i in range(l, r + 1):
            result.append(matrix[t][i])
            num += 1
        t += 1

        for i in range(t, b + 1):
            result.append(matrix[i][r])
            num += 1
        r -= 1

        if num >= len(matrix) * len(matrix[0]):
            break
        for i in range(r, l - 1, -1):
            num += 1
            result.append(matrix[b][i])
        b -= 1

        for i in range(b, t - 1, -1):
            result.append(matrix[i][l])
            num += 1
        l += 1
    print(result)


if __name__ == '__main__':
    spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

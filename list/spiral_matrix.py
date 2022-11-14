#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :spiral_matrix.py.py
# @Time      :2022/10/28 9:51


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        l, r, t, b, x = 0, n - 1, 0, n - 1, 1

        while x <= n * n:
            for i in range(l, r + 1):
                matrix[t][i] = x
                x += 1

            t += 1
            for i in range(t, b + 1):
                matrix[i][r] = x
                x += 1
            r -= 1

            for i in range(r, l - 1, -1):
                matrix[b][i] = x
                x += 1
            b -= 1

            for i in range(b, t - 1, -1):
                matrix[i][l] = x
                x += 1
            l += 1
        return matrix


if __name__ == '__main__':
    s = Solution()
    print(*s.generateMatrix(3), sep='\n')
    print(*s.generateMatrix(4), sep='\n')

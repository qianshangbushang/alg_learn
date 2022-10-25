#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :p2670.py
# @Time      :2022/10/25 14:12

from typing import List


def run():
    n, m = map(int, input().split())
    lines = []
    for _ in range(n):
        lines.append(list(input()))
    print(logic(lines))
    return


def add_matrix(m, r, c):
    if c - 1 >= 0:
        if r - 1 >= 0:
            m[r - 1][c - 1] += 1  # 左上
        m[r][c - 1] += 1  # 左
        if r + 1 <= len(m) - 1:  # 左下
            m[r + 1][c - 1] += 1

    if r - 1 >= 0:
        m[r - 1][c] += 1
    if r + 1 <= len(m) - 1:
        m[r + 1][c] += 1

    if c + 1 <= len(m[0]) - 1:
        if r - 1 >= 0:
            m[r - 1][c + 1] += 1  # 右上
        m[r][c + 1] += 1  # 右
        if r + 1 <= len(m) - 1:
            m[r + 1][c + 1] += 1  # 右下


def logic(matrix: List[List[str]]):
    ret_matrix = [[0 for _ in matrix[0]] for _ in matrix]
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == "*":
                add_matrix(ret_matrix, row, col, )
                # ret_matrix[row][col] = "*"

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == '*':
                ret_matrix[row][col] = "*"
    ret_matrix = "\n".join(["".join([str(x) for x in row]) for row in ret_matrix])
    return ret_matrix


if __name__ == '__main__':
    run()

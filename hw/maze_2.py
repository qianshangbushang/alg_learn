#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :maze_2.py
# @Time      :2022/7/15 21:36

import sys


def run():
    sys.stdin.readline()
    lines = sys.stdin.readlines()
    lines = list(map(lambda x: [int(i) for i in x.strip().split(" ")], lines))
    logic(lines)
    return


def logic(data):
    row, col = len(data), len(data[0])

    def walk(i, j, path=[(0, 0)]):
        if i == row - 1 and j == col - 1:
            for x in path:
                print(f"({x[0], x[1]})")
            return
        if j + 1 < col and data[i][j + 1] == 0:
            if (i, j + 1) not in path:
                walk(i, j + 1, path + [(i, j + 1)])
        if i + 1 < row and data[i + 1][j] == 0:
            if (i + 1, j) not in path:
                walk(i + 1, j, path + [(i + 1, j)])
        if j - 1 > 0 and data[i][j - 1] == 0:
            if (i, j - 1) not in path:
                walk(i, j - 1, path + [(i, j - 1)])
        if i - 1 > 0 and data[i - 1][j] == 0:
            if (i - 1, j) not in path:
                walk(i - 1, j, path + [(i - 1, j)])
        return

    return


run()

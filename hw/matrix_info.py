#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :matrix_info.py
# @Time      :2022/7/18 0:41


import sys
from typing import List


def run():
    n = int(sys.stdin.readline().strip())
    matric_info = {}
    for idx in range(n):
        matric_info[chr(idx + ord('A'))] = list(map(int, sys.stdin.readline().strip().split(" ")))
    expr = sys.stdin.readline().strip()
    # print(matric_info)
    print(logic(matric_info, expr))
    return


def logic(matric_info: dict, expr: str):
    _, _, cnt = computeExpr(matric_info, expr, 0)
    return cnt


def computeExpr(matric_info: dict, expr: str, start):
    arr = []
    idx = start
    cnt = 0
    while idx < len(expr) and expr[idx] != ')':
        if expr[idx] == '(':
            x, idx, num = computeExpr(matric_info, expr, idx + 1)
            arr.append(x)
            cnt += num
            continue
        arr.append(matric_info[expr[idx]])
        idx += 1

    sum_matrix, sum_cnt = cumsum_matrix(arr)
    cnt += sum_cnt
    return sum_matrix, idx + 1, cnt


def cumsum_matrix(data: List[List[int]]):
    if len(data) == 1:
        return data[0], 0
    cnt = 0
    base = data[0]
    for idx in range(1, len(data)):
        x = data[idx]
        cnt += base[0] * base[1] * x[1]
        base = [base[0], x[1]]
    return base, cnt


if __name__ == '__main__':
    matrix_info = {
        "A": [47, 45],
        "B": [45, 31],
        "C": [31, 20],
        "D": [20, 35],
        "E": [35, 59],
        "F": [59, 42],
        "G": [42, 28],
    }
    expr = "(A((B(C(DE)))(FG)))"
    print(logic(matrix_info, expr))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :P1551.py
# @Time      :2022/11/7 9:13


from typing import List


def run():
    return


def logic():
    return


def init(father: dict, rank: dict, all_nodes: List[int]):
    for node in all_nodes:
        father[node] = node
        rank[node] = 1
    return


def find(father: dict, target: int):
    if father[target] == target:
        return target
    return find(father[target])


def merge(father: dict, rank: dict, node1: int, node2: int):
    f1 = find(father, node1)
    f2 = find(father, node2)

    if rank[node1] <= rank[node2]:
        father[f1] = f2
    else:
        father[f2] = f1

    if rank[node1] == rank[node2] and node1 != node2:
        rank[node2] += 1

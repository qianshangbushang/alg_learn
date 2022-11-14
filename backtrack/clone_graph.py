#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :clone_graph.py
# @Time      :2022/11/11 16:50


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return node

        if node.val in self.visited:
            return self.visited[node.val]

        new_node = Node(node.val, [])
        self.visited[node.val] = new_node

        for neibor in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(neibor))
        return new_node

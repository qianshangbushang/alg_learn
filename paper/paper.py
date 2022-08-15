#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :paper.py
# @Time      :2022/7/27 11:47


import torch
from torch import nn


class LayerNorm(nn.Module):
    def __init__(self, dim, eps=1e-6):
        super(LayerNorm, self).__init__()
        self.gamma = torch.nn.Parameter(torch.ones(dim))
        self.beta = torch.nn.Parameter(torch.zeros(dim))
        self.eps = eps

    def forward(self, input: torch.tensor):
        mean = torch.mean()

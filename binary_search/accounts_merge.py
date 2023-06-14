#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :accounts_merge.py
# @Time      :2023/2/2 16:10
from collections import defaultdict
from typing import List

"""
给定一个列表 accounts，每个元素 accounts[i] 是一个字符串列表，其中第一个元素 accounts[i][0] 是 名称 (name)，其余元素是 emails 表示该账户的邮箱地址。
现在，我们想合并这些账户。
    如果两个账户都有一些共同的邮箱地址，则两个账户必定属于同一个人。
    请注意，即使两个账户具有相同的名称，它们也可能属于不同的人，因为人们可能具有相同的名称。一个人最初可以拥有任意数量的账户，但其所有账户都具有相同的名称。
合并账户后，按以下格式返回账户：
    每个账户的第一个元素是名称，其余元素是 按字符 ASCII 顺序排列 的邮箱地址。
    账户本身可以以 任意顺序 返回。
"""
"""
输入：accounts = [
    ["John", "johnsmith@mail.com", "john00@mail.com"], 
    ["John", "johnnybravo@mail.com"], 
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"], 
    ["Mary", "mary@mail.com"]]
输出：[
    ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
    ["John", "johnnybravo@mail.com"], 
    ["Mary", "mary@mail.com"]
    ]
"""


class Recorder:
    def __init__(self):
        self.f_dict = {}
        return

    def add(self, email):
        if email not in self.f_dict:
            self.f_dict[email] = email
        return

    def find(self, email):
        if self.f_dict[email] == email:
            return email
        return self.find(self.f_dict[email])

    def merge(self, email_x, email_y):
        self.f_dict[self.find(email_x)] = self.find(email_y)
        return


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        recorder = Recorder()
        dp_dict = {}
        for idx, account in enumerate(accounts):
            for email in account[1:]:
                recorder.add(email)
                if email not in dp_dict:
                    dp_dict[email] = idx

        for account in accounts:
            if len(account) <= 2:
                continue

            for i in range(2, len(account)):
                recorder.merge(account[i], account[i - 1])

        result_dict = defaultdict(list)
        for item, account in recorder.f_dict.items():
            result_dict[dp_dict[recorder.find(item)]].append(item)

        result_list = []
        for key, arr in result_dict.items():
            result_list.append([accounts[key][0]] + sorted(arr))

        return result_list


if __name__ == '__main__':
    s = Solution()
    accounts = [
        ["John", "johnsmith@mail.com", "john00@mail.com"],
        ["John", "johnnybravo@mail.com"],
        ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
        ["Mary", "mary@mail.com"]
    ]
    print(s.accountsMerge(accounts))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :partition_label.py
# @Time      :2022/7/1 14:24


from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if len(s) == 0:
            return []

        pos_dict = [0] * 26
        for idx, ch in enumerate(s):
            pos_dict[ord(ch) - ord('a')] = idx

        result = []
        left = 0
        right = pos_dict[ord(s[0]) - ord('a')]
        for idx, ch in enumerate(s):
            right = max(right, pos_dict[ord(ch) - ord('a')])
            if right == idx:
                result.append(right - left + 1)
                left = right + 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.partitionLabels("ababcbacadefegdehijhklij"))

#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :common_char.py
# @Time      :2022/7/7 11:16


from typing import List


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        1002. https://leetcode.cn/problems/find-common-characters/
        输入：words = ["bella","label","roller"]
        输出：["e","l","l"]
        :param words:
        :return:
        """
        hash_map = [[0 for _ in range(26)] for _ in range(len(words))]

        for idx, word in enumerate(words):
            for ch in word:
                hash_map[idx][ord(ch) - 97] += 1

        result = []
        for pos in range(26):
            min_val = 26
            for idx in range(len(words)):
                min_val = min(hash_map[idx][pos], min_val)
                if not min_val:
                    continue
            while min_val > 0:
                result.append(chr(pos + 97))
                min_val -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.commonChars(["bella", "label", "roller"]))

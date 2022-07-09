#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :len_of_substr.py
# @Time      :2022/7/8 23:25


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0

        cnt_map = {}
        max_len = 0
        while end < len(s):
            while s[end] in cnt_map:
                del cnt_map[s[start]]
                start += 1
            cnt_map[s[end]] = 1
            max_len = max(max_len, len(cnt_map))
            end += 1
        return max_len


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))

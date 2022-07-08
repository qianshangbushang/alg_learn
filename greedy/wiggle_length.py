#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :wiggle_length.py
# @Time      :2022/7/8 10:53


from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        """
        a: 上一次是上升的最大长度
        b: 上一次是下降的最大长度
        :param nums:
        :return:
        """
        a, b = 1, 1
        for idx in range(1, len(nums)):
            if nums[idx] - nums[idx - 1] > 0:
                a = max(a, b + 1)
            if nums[idx] - nums[idx - 1] < 0:
                b = max(b, a + 1)
        return max(a, b)

    def wiggleMaxLength1(self, nums: List[int]) -> int:
        """
        循环选择峰和谷，可以找到最终结果

        如果中间还存在元素，满足  峰 》 当前元素 》 谷，  选择没问题
        如果中间还存在元素, 满足 峰 《 当前元素， 谷 《 当前元素， 则 峰和谷退化成谷，当前元素为峰

        当只有两个元素时，如果不相等，则一为峰，一为谷

        计算当前元素c，只需考虑前两元素a, b 如果a <b > c, c 为谷，
                                      如果a < b <= c, c不计算
        只有反转了才记录方向
        :param nums:
        :return:
        """

        if len(nums) < 2:
            return len(nums)

        pre_diff = nums[1] - nums[0]
        result = 2 if pre_diff != 0 else 1

        for idx in range(2, len(nums)):
            cur_diff = nums[idx] - nums[idx - 1]
            if pre_diff >= 0 and cur_diff < 0:
                result += 1
                pre_diff = cur_diff

            if pre_diff <= 0 and cur_diff > 0:
                result += 1
                pre_diff = cur_diff
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.wiggleMaxLength([1, 7, 4, 9, 2, 5]))
    print(s.wiggleMaxLength([1, 17, 5, 10, 13, 15, 10, 5, 16, 8]))

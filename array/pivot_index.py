from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        all_sum = sum(nums)
        pre_sum = 0
        for idx, x in enumerate(nums):
            suf_sum = all_sum - pre_sum - x
            if suf_sum == pre_sum:
                return idx
        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.pivotIndex([2, 1, -1]))

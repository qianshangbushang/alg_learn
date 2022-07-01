from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        last, min_len = 0, 0
        for fast in range(len(nums)):
            target -= nums[fast]

            while target <= 0:
                if not min_len or min_len > fast - last + 1:
                    min_len = fast - last + 1
                target += nums[last]
                last += 1
        return min_len


if __name__ == '__main__':
    s = Solution()
    print(s.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))

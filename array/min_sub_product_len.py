from typing import List


# 10    -> 1  10
# 10 5  -> 2  [5], [10, 5]
# 10 5 2 -> 5 2 -> 2,  [2] [5, 2]
# 5 2 6 -> 3 [2,6], [5, 2, 6], [6]


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        last, cnt, product = 0, 0, 1
        for fast in range(len(nums)):
            product *= nums[fast]
            if product < k:
                cnt += fast - last + 1
                continue
            while product >= k:
                product /= nums[last]
                last += 1
                if product < k:
                    cnt += fast - last + 1
        return cnt


if __name__ == '__main__':
    s = Solution()
    print(s.numSubarrayProductLessThanK([10, 5, 2, 6], 100))

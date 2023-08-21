from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        pre_sum_max, pre_sum_min, sum = 0, 0, 0
        result = 0
        for x in nums:
            sum += x
            pre_sum_max = max(pre_sum_max, sum)
            pre_sum_min = min(pre_sum_min, sum)
            result = max(result, pre_sum_max - pre_sum_min)
        return result
    


class Solution2:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        n_sum, p_sum, max_sum=0, 0, 0
        for x in nums:
            n_sum = min(0, n_sum + x)
            p_sum = max(0, p_sum + x)
            max_sum = max(-n_sum, p_sum, max_sum)
        return max_sum




if __name__ == "__main__":
    s = Solution()
    print(s.maxAbsoluteSum([2,-5,1,-4,3,-2]))
    print(s.maxAbsoluteSum([1,-3,2,3,-4]))

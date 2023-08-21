"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

"""


from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(start):
            if start == len(nums) - 1:
                result.append(nums[:])
                return

            for i in range(start , len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1, )
                nums[start], nums[i] = nums[i], nums[start]
        backtrack(0)
        return result
    


if __name__ == "__main__":
    s = Solution()
    print(s.permute([1, 2, 3]))
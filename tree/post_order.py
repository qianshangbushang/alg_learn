from posixpath import split
from re import T
from turtle import right
from typing import List

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if len(postorder) <= 1 :
            return True
        cur_node = postorder[len(postorder) - 1]
        split  = self.find_split(postorder, cur_node)
        left_part = postorder[:split]
        right_part = postorder[split: len(postorder) - 1]

        # left_not_ok = any (x > cur_node for x in left_part) 

        if any(x < cur_node for x in right_part):
            return False
        return self.verifyPostorder(left_part) and self.verifyPostorder(right_part)

    def find_split(self, l, v):
        for i in range(len(l)):
            if l[i] > v:
                return i
        return len(l)  - 1



if __name__ == "__main__":
    s = Solution()
    print(s.verifyPostorder([4, 6, 7, 5]))
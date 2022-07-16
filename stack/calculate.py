class Solution:
    def calculate(self, s: str) -> int:
        arr = []

        pre_sign, i = '+', 0
        curr_num = 0
        s = s + "+"
        while i < len(s):
            if '0' <= s[i] <= '9':
                curr_num = curr_num * 10 + (ord(s[i]) - ord('0'))
                i += 1
                continue

            if s[i] not in ['+', '-', '*', '/']:
                i += 1
                continue

            # 碰到符号了
            if pre_sign == "+":
                arr.append(curr_num)
            elif pre_sign == "-":
                arr.append(-curr_num)
            elif pre_sign == "*":
                arr[-1] = arr[-1] * curr_num
            else:
                arr[-1] = int(arr[-1] / curr_num)
            curr_num = 0
            pre_sign = s[i]
            i += 1
        return sum(arr)

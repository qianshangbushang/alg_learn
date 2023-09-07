# Alice 和 Bob 计划分别去罗马开会。
# 给你四个字符串 arriveAlice ，leaveAlice ，arriveBob 和 leaveBob 。
# Alice 会在日期 arriveAlice 到 leaveAlice 之间在城市里（日期为闭区间），
# 而 Bob 在日期 arriveBob 到 leaveBob 之间在城市里（日期为闭区间）。
# 每个字符串都包含 5 个字符，格式为 "MM-DD" ，对应着一个日期的月和日。
#
# 请你返回 Alice和 Bob 同时在罗马的天数。
#
# 你可以假设所有日期都在 同一个 自然年，而且 不是 闰年。
# 每个月份的天数分别为：[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 。


month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        a_min_day, a_max_day = self.compute_duration(arriveAlice, leaveAlice)
        b_min_day, b_max_day = self.compute_duration(arriveBob, leaveBob)

        result = min(a_max_day, b_max_day) - max(a_min_day, b_min_day)  + 1
        return result if  result > 0 else 0

    def compute_duration(self, arrive: str, leave: str):
        a_mon, a_day = map(int, arrive.split("-"))
        l_mon, l_day = map(int, leave.split("-"))

        min_day = sum(month_days[:a_mon]) + a_day
        max_day = sum(month_days[:l_mon]) + l_day

        return min_day, max_day


if __name__ == "__main__":
    s = Solution()
    print(s.countDaysTogether(arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"))
    print(s.countDaysTogether(arriveAlice = "10-01", leaveAlice = "10-31", arriveBob = "11-01", leaveBob = "12-31"))
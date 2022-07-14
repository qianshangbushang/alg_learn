"""
输入的第 1 行，为两个正整数N，m，用一个空格隔开：
（其中 N （ N<32000 ）表示总钱数， m （m <60 ）为可购买的物品的个数。）
从第 2 行到第 m+1 行，第 j 行给出了编号为 j-1 的物品的基本数据，每行有 3 个非负整数 v p q
（其中 v 表示该物品的价格（ v<10000 ）， p 表示该物品的重要度（ 1 ~ 5 ）， q 表示该物品是主件还是附件。
    如果 q=0 ，表示该物品为主件，如果 q>0 ，表示该物品为附件， q 是所属主件的编号）
"""
import sys


def read_param():
    first = sys.stdin.readline().strip().split(" ")
    N, m = int(first[0]), int(first[1])  # N < 32000, m < 60
    lines = sys.stdin.readlines()
    lines = [[int(y) for y in x.strip().split(" ")] for x in lines]
    for idx in range(len(lines)):
        lines[idx][0] = lines[idx][0] // 10
    return N // 10, m, lines


def generate_attach_dict(raw_item_list):
    attach_price = {}
    attach_value = {}

    # 先存放主件
    for idx in range(len(raw_item_list)):
        [p, v, q] = raw_item_list[idx]
        curr_price = int(p)
        curr_value = int(v * p * 10)
        if q != 0:  # 附件的情况
            continue
        attach_price[idx + 1] = [curr_price, 0, 0]  # 价格表: 主件, 附件1, 附件2
        attach_value[idx + 1] = [curr_value, 0, 0]  # 价值表: 主件, 附件1, 附件2

    # 存放附件
    for idx in range(len(raw_item_list)):
        [p, v, q] = raw_item_list[idx]
        curr_price = int(p)
        curr_value = int(v * p * 10)
        if q == 0:  # 主件
            continue
        if attach_price[q][1] == 0:  # 附件1
            attach_price[q][1] = curr_price
            attach_value[q][1] = curr_value
            continue
        # 附件2
        attach_price[q][2] = curr_price
        attach_value[q][2] = curr_value
    return attach_price, attach_value


def run():
    total_fee, total_items, raw_item_list = read_param()
    attach_price, attach_value = generate_attach_dict(raw_item_list)
    # print(attach_price)
    # print(attach_value)
    # dp[j] 表示资金为j，能获取的最大价值
    # 对物品i而言， dp[j] = dp[j - price[i]] + value[i]
    # 每个件只能放一次，所以先遍历物件
    dp = [0] * (total_fee + 1)
    for primary_id in attach_price.keys():
        # print(primary_id)
        curr_money = total_fee
        while curr_money >= attach_price[primary_id][0]:  # 必须要能购买主件
            # 只购买主件
            left_money = curr_money - attach_price[primary_id][0]
            make_value = attach_value[primary_id][0]
            dp[curr_money] = max(dp[curr_money], dp[left_money] + make_value)

            # 购买主件 + 附件1
            left_money = curr_money - attach_price[primary_id][0] - attach_price[primary_id][1]
            make_value = attach_value[primary_id][0] + attach_value[primary_id][1]
            if left_money >= 0:
                dp[curr_money] = max(dp[curr_money], dp[left_money] + make_value)

            # 购买主件 + 附件2
            left_money = curr_money - attach_price[primary_id][0] - attach_price[primary_id][2]
            make_value = attach_value[primary_id][0] + attach_value[primary_id][2]
            if left_money >= 0:
                dp[curr_money] = max(dp[curr_money], dp[left_money] + make_value)

            # 购买主件 + 附件2 + 附件3
            left_money = curr_money - sum(attach_price[primary_id])
            make_value = sum(attach_value[primary_id])
            if left_money >= 0:
                dp[curr_money] = max(dp[curr_money], dp[left_money] + make_value)
            curr_money -= 1
    # print(dp)
    print(dp[-1])
    return


if __name__ == '__main__':
    run()

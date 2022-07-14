import re
import sys


def is_valid(s: str):
    if len(s) <= 8:
        return False

    sub = []
    for i in range(0, len(s) - 3):
        if s[i:i + 3] in sub:
            return False
        sub.append(s[i:i + 3])

    upper = '[A-Z]'
    lowwer = '[a-z]'
    num = '\d'
    chars = '[^A-Za-z0-9]'

    cond_valid = 0
    for p in [upper, lowwer, num, chars]:
        pw = re.search(p, s)
        if pw: cond_valid += 1
    if cond_valid < 3:
        return False
    return True


def run():
    lines = sys.stdin.readlines()
    lines = [x.strip() for x in lines]
    for line in lines:
        if is_valid(line):
            print("OK")
        else:
            print("NG")
    return


run()

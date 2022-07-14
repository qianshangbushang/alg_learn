import sys


def read_param():
    line = sys.stdin.readline().strip()
    result = [0, 0]
    for action in line.split(";"):
        if len(action) <= 1 or len(action) > 3:
            continue

        cmd = action[0]
        step = action[1:]

        if not step.isdigit():
            continue
        if cmd == 'A':
            result[0] -= int(step)
            continue
        if cmd == "D":
            result[0] += int(step)
        if cmd == "W":
            result[1] += int(step)
        if cmd == "S":
            result[1] -= int(step)
    print(",".join([str(x) for x in result]))


read_param()
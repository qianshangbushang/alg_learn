

def spiral_matrix(m:int, n:int):
    max_num = m * n 
    l, r, t, b, num = 0, n-1, 0, m-1, 1

    ret = [[0 for _ in range(n)] for _ in range(m)]
    while  num <= max_num:
        for i in range(l, r+1):
            ret[t][i] = num
            num += 1
        t += 1
        for i in range(t, b+1):
            ret[i][r] = num
            num += 1
        r -= 1
        if num > max_num:
            break
        for i in range(r, l-1, -1):
            ret[b][i] = num
            num += 1
        b -= 1
        for i in range(b, t-1, -1):
            ret[i][l] = num
            num += 1
        l += 1
    return ret


if __name__ == "__main__":
    print(*(spiral_matrix(4, 4)), sep='\n')
    print("\n")
    print(*(spiral_matrix(3, 4)), sep='\n')
    print("\n")
    print(*(spiral_matrix(4, 3)), sep='\n')
        



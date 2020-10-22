arr = [1, 2, 3]
N = 3
R = 3

sel = [0] * R


def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i + 1, sidx + 1)


combination(0, 0)
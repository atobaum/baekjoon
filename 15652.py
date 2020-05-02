def solve(cur, remain, notUsed):
    if remain == 0:
        print(" ".join(cur))
    else:
        for i, c in enumerate(notUsed):
            solve(cur + [c], remain - 1, notUsed[i:])

N, M = map(int, input().split())
solve([], M, list(map(str, range(1, N+1))))

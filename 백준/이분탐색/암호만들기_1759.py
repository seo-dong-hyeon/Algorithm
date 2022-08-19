from itertools import combinations

L, C = map(int, input().split())
alphabets = sorted(list(input().split()))
nCr = combinations(alphabets, L)

for combination in nCr:
    moeumCnt = 0
    jaeumCnt = 0
    for c in combination:
        if c in ['a', 'e', 'i', 'o', 'u']:
            moeumCnt += 1
        else:
            jaeumCnt += 1
    if moeumCnt < 1 or jaeumCnt < 2:
        continue
    print("".join(sorted(list(combination))))
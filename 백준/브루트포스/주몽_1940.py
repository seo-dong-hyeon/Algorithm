# 투포인터로 개선 필요

import sys

N = int(sys.stdin.readline().rstrip())
M = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

nums.sort()
answer = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if i == j:
            continue
        if nums[i] + nums[j] > M:
            break
        if nums[i] + nums[j] == M:
            answer += 1

print(answer)
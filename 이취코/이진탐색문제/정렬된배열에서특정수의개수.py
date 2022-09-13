import sys
from bisect import bisect_left, bisect_right

N, x = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

answer = bisect_right(nums, x) - bisect_left(nums, x)
print(answer if answer != 0 else -1)
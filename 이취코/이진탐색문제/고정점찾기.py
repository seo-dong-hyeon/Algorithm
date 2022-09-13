# 고정점 찾기 문제
# 정렬 -> 이분탐색
import sys

N = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = N
answer = -1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == mid:
        answer = mid
        break
    elif nums[mid] > mid:
        right = mid - 1
    else:
        left = mid + 1

print(answer)

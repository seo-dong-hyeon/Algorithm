import sys

N, K = map(int, sys.stdin.readline().rstrip().split())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

left = 0
right = K
# 초기값
num_sum = sum(nums[left:right])
max_sum = num_sum

while right < N:
    # 값 갱신(왼쪽꺼 빼고 오른쪽꺼 더함) 후 비교
    num_sum = num_sum + nums[right] - nums[left]
    max_sum = max(max_sum, num_sum)
    # 인덱스 갱신
    right += 1
    left += 1

print(max_sum)

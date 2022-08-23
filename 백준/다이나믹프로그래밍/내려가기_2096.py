# 다이나믹 프로그래밍 - 내려가기
# 메모이제이션 - 이전값이 필요없음 -> 한 줄에 저장
N = int(input())
nums = []
dp_max = [0] * 3
dp_min = [0] * 3

nums = list(map(int, input().split()))
dp_max[0], dp_max[1], dp_max[2] = nums[0], nums[1], nums[2]
dp_min[0], dp_min[1], dp_min[2] = nums[0], nums[1], nums[2]

for _ in range(1, N):
    nums = list(map(int, input().split()))
    dp_max[0], dp_max[1], dp_max[2] = nums[0] + max(dp_max[0], dp_max[1]), nums[1] + max(dp_max[0], dp_max[1], dp_max[2]), nums[2] + max(dp_max[1], dp_max[2])
    dp_min[0], dp_min[1], dp_min[2] = nums[0] + min(dp_min[0], dp_min[1]), nums[1] + min(dp_min[0], dp_min[1], dp_min[2]), nums[2] + min(dp_min[1], dp_min[2])

print(max(dp_max), min(dp_min))
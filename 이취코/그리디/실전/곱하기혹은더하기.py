import sys

S = sys.stdin.readline().rstrip()

nums = []
for i in range(len(S)):
    nums.append(int(S[i]))

max_val = nums[0]
for i in range(1, len(nums)):
    max_val = max(max_val * nums[i], max_val + nums[i])
print(max_val)
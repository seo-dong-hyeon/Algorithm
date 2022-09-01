import sys

S = sys.stdin.readline().rstrip()
alpha = []
nums = []

for i in range(len(S)):
    if S[i].isalpha():
        alpha.append(S[i])
    else:
        nums.append(int(S[i]))
alpha.sort()

print("".join(alpha) + "" + str(sum(nums)))

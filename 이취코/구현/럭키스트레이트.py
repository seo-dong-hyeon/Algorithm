import sys

N = sys.stdin.readline().rstrip()
left = 0
right = 0
mid = len(N) // 2

for i in range(len(N)):
    if i < mid:
        left += int(N[i])
    else:
        right += int(N[i])

print("LUCKY" if left == right else "READY")
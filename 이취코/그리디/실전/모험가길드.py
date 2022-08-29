import sys

X = list(map(int, sys.stdin.readline().rstrip().split()))
X.sort()    # 1 2 2 2 3

answer = 0
group = []
for i in range(len(X)):
    group.append(X[i])
    if len(group) >= X[i]:
        answer += 1
        group = []

print(answer)
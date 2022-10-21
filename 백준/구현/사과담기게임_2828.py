import sys

N, M = map(int, sys.stdin.readline().rstrip().split())
J = int(sys.stdin.readline().rstrip())

apples = []
for _ in range(J):
    apples.append(int(sys.stdin.readline().rstrip()))

pos = [1, M]
answer = 0
for apple in apples:
    # 왼쪽
    if apple < pos[0]:
        dist = pos[0] - apple
        pos[0] -= dist
        pos[1] -= dist
    # 오른쪽
    elif apple > pos[1]:
        dist = apple - pos[1]
        pos[0] += dist
        pos[1] += dist
    else:
        dist = 0
    answer += dist

print(answer)

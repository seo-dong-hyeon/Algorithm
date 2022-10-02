# 누적 합 - imos법
import sys

A, B, C = map(int, sys.stdin.readline().rstrip().split())
prefix_sum = [0] * 102
answer = 0

# 입장(s)과 퇴장(e)만 기록
for _ in range(3):
    s, e = map(int, sys.stdin.readline().rstrip().split())
    prefix_sum[s] += 1
    prefix_sum[e] -= 1

# 한 번에 쓸면서 누적합 계산
for i in range(len(prefix_sum) - 1):
    prefix_sum[i + 1] += prefix_sum[i] 

for i in range(len(prefix_sum) - 1):
    if prefix_sum[i] == 1:
        answer += (prefix_sum[i] * A)
    elif prefix_sum[i] == 2:
        answer += (prefix_sum[i] * B)
    elif prefix_sum[i] == 3:
        answer += (prefix_sum[i] * C)

# print(prefix_sum)

print(answer)
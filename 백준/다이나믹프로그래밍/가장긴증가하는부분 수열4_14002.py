import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
# dp[i] -> i번까지 가장 긴 증가하는 수열 길이
dp = [1] * N

for i in range(1, N):
    for j in range(i):
        # 기준점 위치가 이전 탐색 수보다 크다면
        if A[i] > A[j]:
            dp[i] = max(dp[i], dp[j] + 1)

# 최대 길이
max_dp = max(dp)
print(max_dp)

# 뒤에서부터 탐색하면서
# 증가하는 길이와 일치하는 원소들 저장
answer = []
for i in range(N - 1, -1, -1):
    if dp[i] == max_dp:
        answer.append(A[i])
        max_dp -= 1

answer.reverse()
for num in answer:
    print(num, end=' ')
print()
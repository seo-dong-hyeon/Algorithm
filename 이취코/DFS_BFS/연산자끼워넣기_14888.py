# DFS - 여러 갈래 길
import sys

def dfs(idx, plus, minus, multi, div, sum):
    if idx == N:
        global max_sum, min_sum
        max_sum = max(max_sum, sum)
        min_sum = min(min_sum, sum)
        return

    if plus > 0:
        dfs(idx + 1, plus - 1, minus, multi, div, sum + A[idx])
    if minus > 0:
        dfs(idx + 1, plus, minus - 1, multi, div, sum - A[idx])
    if multi > 0:
        dfs(idx + 1, plus, minus, multi - 1, div, sum * A[idx])
    if div > 0:
        sum = sum // A[idx] if sum > 0 else ((sum * -1) // A[idx]) * -1
        dfs(idx + 1, plus, minus, multi, div - 1, sum)
    return

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
plus, minus, multi, div = map(int, sys.stdin.readline().split())
max_sum = 1e10 * -1
min_sum = 1e10

dfs(1, plus, minus, multi, div, A[0])
print(max_sum, min_sum)
# 펜윅트리
# 리스트의 값이 자주 바뀌는 상황에서
# 리스트에서 어느 구간의 구간합을 구할 때

import sys

N, M, K = map(int, sys.stdin.readline().split())
nums = []
# 전체 트리 사이즈 = 리스트 x 4
tree = [0] * N * 4


# 트리 생성
def init(left, right, node):
    if left == right:
        tree[node] = nums[left]
        return
    else:
        mid = (left + right) // 2
        init(left, mid, node * 2)
        init(mid + 1, right, node * 2 + 1)
        tree[node] = tree[node * 2] + tree[node * 2 + 1]


# 리스트 업데이트
def update(left, right, node, idx, diff):
    if idx < left or idx > right:
        return
    tree[node] += diff
    if left == right:
        return
    mid = (left + right) // 2
    update(left, mid, node * 2, idx, diff)
    update(mid + 1, right, node * 2 + 1, idx, diff)


# 구간합 구하기
def sum(left, right, node, start, end):
    if start > right or end < left:
        return 0
    if start <= left and right <= end:
        return tree[node]
    mid = (left + right) // 2
    return sum(left, mid, node * 2, start, end) + sum(mid + 1, right, node * 2 + 1, start, end)


N, M, K = map(int, sys.stdin.readline().split())
nums = []
for i in range(N):
    nums.append(int(sys.stdin.readline()))

init(0, N - 1, 1)

for i in range(M + K):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        diff = c - nums[b - 1]
        nums[b - 1] = c
        update(0, N - 1, 1, b - 1, diff)
    else:
        print(sum(0, N - 1, 1, b - 1, c - 1))

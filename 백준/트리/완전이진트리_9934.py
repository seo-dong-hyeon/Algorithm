import sys

k = int(sys.stdin.readline().rstrip())
nodes = list(map(int, sys.stdin.readline().rstrip().split()))
answer = [[] for _ in range(k)]

def dfs(nodes, depth):
    # 트리의 root index를 찾아낸다.
    mid = (len(nodes) // 2)

    # 해당 깊이에 해당하는 node를 추가한다.
    answer[depth].append(nodes[mid])

    if len(nodes) == 1:
        return

    dfs(nodes[:mid], depth+1)
    dfs(nodes[mid + 1:], depth+1)

dfs(nodes, 0)

for i in answer:
    print(*i)
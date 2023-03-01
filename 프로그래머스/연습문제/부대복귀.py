# 다익스트라
from collections import deque

def solution(n, roads, sources, destination):
    answer = []

    graph = [[] for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append([1, b])
        graph[b].append([1, a])

    distances = [1e9] * (n + 1)

    dq = deque()
    dq.append([0, destination])
    distances[destination] = 0
    while dq:
        dist, node = dq.popleft()
        if distances[node] < dist:
            continue
        for next_dist, next_node in graph[node]:
            cost = dist + next_dist
            if distances[next_node] > cost:
                dq.append([cost, next_node])
                distances[next_node] = cost

    for source in sources:
        answer.append(distances[source] if distances[source] != 1e9 else -1)

    return answer
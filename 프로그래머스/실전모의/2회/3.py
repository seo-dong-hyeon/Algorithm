import heapq

# 다익스트라
def solution(n, roads, sources, destination):
    answer = []
    graph = [[] * (n + 1) for _ in range(n + 1)]
    
    for road in roads:
        graph[road[0]].append([1, road[1]]) 
        graph[road[1]].append([1, road[0]])

    distances = [1e9] * (n + 1)
    distances[destination] = 0
    hq = []
    heapq.heappush(hq, [0, destination])

    while hq:
        dist, node = heapq.heappop(hq)
        if distances[node] < dist:
            continue
        distances[node] = dist
        for next_dist, next_dest in graph[node]:
            cost = next_dist + dist
            if distances[next_dest] > cost:
                distances[next_dest] = cost
                heapq.heappush(hq, [cost, next_dest])

    for source in sources:
        answer.append(distances[source] if distances[source] != 1e9 else -1)


    return answer
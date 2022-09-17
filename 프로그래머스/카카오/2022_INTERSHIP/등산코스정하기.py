# 다익스트라
# cost 기준 -> 누적합 X, 각 길이 중 최대값
import heapq

def solution(n, paths, gates, summits):
    answer = []
    
    # 간선 초기화
    graph = [[] * (n + 2) for _ in range(n + 2)]
    for i, j, w in paths:
        graph[i].append([w, j])
        graph[j].append([w, i])

    summits.sort()
    set_summit = set()
    for summit in summits:
        set_summit.add(summit)

    # intensity 초기화
    # intensities[i] = 출발지에서 i로 가는 최대 intensity
    intensities = [1e9] * (n + 2)

    # 모든 출입구를 heap에 넣음
    heqp = []
    for gate in gates:
        heapq.heappush(heqp, [0, gate])
        intensities[gate] = 0

    # 다익스트라
    while heqp:
        intensity, node = heapq.heappop(heqp)
        # 산봉우리이거나 이미 최적의 값이면 이동 안함
        if node in set_summit or intensities[node] < intensity:
            continue
        # 다음 장소로 이동하면서
        # 현재 intensity와 다음 intensity 중 더 큰 값이 다음 장소의 intensity
        for next_intensity, next_node in graph[node]:
            cost = max(intensity, next_intensity)            
            if cost < intensities[next_node]:
                intensities[next_node] = cost
                heapq.heappush(heqp, [cost, next_node])

    # 산봉우리를 기준으로
    # 가장 intensity가 작은 값을 선택
    answer = [0, 1e9]
    for summit in summits:
        if answer[1] > intensities[summit]:
            answer[0] = summit
            answer[1] = intensities[summit]

    return answer

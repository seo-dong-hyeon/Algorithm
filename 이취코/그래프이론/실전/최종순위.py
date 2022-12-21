# 정확한 순위 문제(기존 순위와 변경된 일부 순위를 주어졌을 때, 바뀐 최종 순위 구하기)
# 위상정렬
'''
1.기존 순위
    -특정 노드에 대해 자신보다 순위가 낮은 등수를 모두 가리키도록 graph 설정
2.변경된 일부 순위
    -graph 간선 방향, indegree 변경
3.위상정렬 수행
4.정확한 순위 -> 정확히 n번만 수행
5.매 분기마다
    -데큐에 원소가 없음 : 사이클 존재 -> 불가능한 경우
    -데큐에 원소가 2개 이상 : 정렬 결과 여러 개 존재 -> 정확한 순위 불가
'''

from collections import deque
import sys

tc = int(sys.stdin.readline().rstrip())
for test_case in range(tc):
    n = int(sys.stdin.readline().rstrip())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for _ in range(n + 1)]

    # 작년 순위
    rank = list(map(int, sys.stdin.readline().rstrip().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[rank[i]][rank[j]] = True
            indegree[rank[j]] += 1

    # 올해 변경된 순위
    m = int(sys.stdin.readline().rstrip())
    for i in range(m):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        # 간선 방향 뒤집기
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[a] += 1
            indegree[b] -= 1
        else:
            graph[a][b] = True
            graph[b][a] = False
            indegree[a] -= 1
            indegree[b] += 1

    # 위상정렬
    answer = []
    dq = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            dq.append(i)

    certain = True  # 순위 결과가 오직 하나
    cycle = False   # 사이클 존재 여부
    # 정확한 순위 -> 정확히 n개만큼만 반복
    for i in range(n):
        # 데큐에 노드가 없으면 사이클 존재
        if len(dq) == 0:
            cycle = True
            break
        # 데큐에 2개 이상의 원소 -> 정렬 결과 여러 개 존재 -> 정확한 순위 불가
        if len(dq) >= 2:
            certain = False
            break
        now = dq.popleft()
        answer.append(now)
        # 해당 노드와 연결된 노드들 진입차수 1 빼기
        for j in range(1, n + 1):
            if graph[now][j]:
                indegree[j] -= 1
                if indegree[j] == 0:
                    dq.append(j)

    if cycle:
        print("IMPOSSIBLE")
    elif not certain:
        print("?")
    else:
        for i in answer:
            print(i, end=' ')
        print()

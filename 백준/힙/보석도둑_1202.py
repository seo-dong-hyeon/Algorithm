# 그리디 - 두 개의 기준
# 무게가 M 이하인 것 들 중, 가치 V가 가장 높은 것
# i번 가방에 넣을 보석 정하기
# i번 가방에 담을 수 있는 보석들을 heap 배열에
# i번 가방에 담을 수 없는 보석이 나오면 heap 배열에서 가장 가치 있는거 선택
# i + 1번 가방에 넣을 보석 정하기...
import sys
import heapq

N, K = map(int, sys.stdin.readline().split())
jewels = []
C = []
heap = []

# 보석 - [무게, 가치] -> 무게 기준 오름차순 정렬
# 가방 - 담을 수 있는 무게 기준 오름차순 정렬
for i in range(N):
    M, V = map(int, sys.stdin.readline().split())
    jewels.append([M, V])

for i in range(K):
    C.append(int(sys.stdin.readline()))

jewels.sort()
C.sort()

answer = 0
idx = 0
for i in range(len(C)):                 # 모든 가방에 대해서 탐색
    for j in range(idx, len(jewels)):   # idx 번 이후 보석만 탐색(이전 보석들은 이미 heap 배열에)
        if jewels[j][0] > C[i]:         # 가방보다 무거운 보석이 나오면
            idx = j                     # 해당 idx 저장 후 앞으로 해당 idx 보석부터 탐색
            break
        heapq.heappush(heap, -jewels[j][1]) # 가방보다 가벼운 보석이 나오면 음수 취한 후 heap 배열에
        idx = j + 1
    
    if len(heap) > 0:                       # heap이 비어있지 않으면 하나 선택
        answer += heapq.heappop(heap) * -1
    elif idx >= len(jewels):                # heap이 비었으면서 더 이상 탐색할 보석이 없다면 종료
        break

print(answer)


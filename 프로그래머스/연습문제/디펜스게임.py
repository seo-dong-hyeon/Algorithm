import heapq

def solution(n, k, enemy):
    answer = 0
    # 디펜스가 적의 라운드보다 많은 경우
    if k >= len(enemy):
        return len(enemy)
    
    # 우선 k라운드까지 디펜스로 막았다고 가정
    answer += k 
    heap = enemy[:k]
    heapq.heapify(heap)

    # k라운드 이후부터 가장 적은 enemy를 병사로 방어했다고 가정
    # 새로 탐색하는 enemy가 힙에 있는 enemy보다 크다면 힙에 저장(디펜스로 막음)
    # 아니면 병사로 막음
    for i in range(k, len(enemy)):
        if heap[0] > enemy[i]:
            if n - enemy[i] < 0:
                break
            n -= enemy[i]
        else:
            heapq.heappush(heap, enemy[i])
            last = heapq.heappop(heap)
            if n - last < 0:
                break
            n -= last
        answer += 1

    return answer


print(solution(7,	3,	[4, 2, 4, 5, 3, 3, 1]))
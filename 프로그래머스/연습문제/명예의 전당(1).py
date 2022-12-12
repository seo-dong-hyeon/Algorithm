import heapq

def solution(k, score):
    answer = []
    heap = []

    for i in range(len(score)):
        if len(heap) < k:
            heapq.heappush(heap, score[i])
        else:
            if score[i] > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, score[i])
        answer.append(heap[0])

    return answer
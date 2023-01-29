import heapq

# 현재 숫자의 뒤를 탐색하며 뒷 큰수 조사 x
# 현재 숫자를 기준으로 앞을 탐색하며 아직 뒷 큰수가 없는 숫자들을 조사
# 아직 뒷 큰수가 없는 숫자들을 탐색의 속도를 위해 heap으로 저장
#   현재 숫자가 탐색 숫자보다 크다면 해당 숫자의 뒷 큰수로 현재 숫자를 저장(해당 숫자의 인덱스를 통해)
#   현재 숫자가 탐색 숫자보다 작다면 종료
# heap에 [현재 숫자, 인덱스]를 저장
def solution(numbers):
    answer = [-1] * len(numbers)

    heap = []
    # 모든 숫자들을 기준으로
    for i, number in enumerate(numbers):
        while heap:
            # 힙에 저장된 숫자가 현재 숫자보다 크거나 같다면 종료
            if heap[0][0] >= number:
                break
            # 힙에 저장된 숫자가 현재 숫자보다 작다면
            # 해당 숫자의 뒷 큰수 값으로 현재 숫자 저장
            _, idx = heapq.heappop(heap)
            answer[idx] = number
        heapq.heappush(heap, [number, i])

    return answer


print(solution([2, 3, 3, 5]))
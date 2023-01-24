import heapq

def solution(ability, number):
    answer = 0

    heapq.heapify(ability)
    for _ in range(number):
        _sum = heapq.heappop(ability) + heapq.heappop(ability)
        heapq.heappush(ability, _sum)
        heapq.heappush(ability, _sum)

    for i in ability:
        answer += i

    return answer


print(solution([10, 3, 7, 2], 2))
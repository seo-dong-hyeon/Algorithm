from collections import deque

def solution(queue1, queue2):
    answer = 0
    flag = False
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    sum_total = sum1 + sum2
    if sum_total % 2 != 0:
        return -1

    length = len(queue1) * 2 + 2
    # 속도를 위해 데큐로 변경
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    while answer <= length:     # 모든 큐의 원소 수만큼 왔다갔다 했다면 더 이상 방법 X
        # 두 큐의 합이 같다면 종료
        if sum1 == sum2:
            flag = True
            break
        # 큐의 합이 더 큰 쪽의 원소를 빼서
        # 작은 쪽에 추가
        # 합을 기록
        elif sum1 > sum2:
            top = queue1.popleft()
            queue2.append(top)
            sum1 -= top
            sum2 += top
        else:
            top = queue2.popleft()
            queue1.append(top)
            sum1 += top
            sum2 -= top
        answer += 1
        
    if not flag:
        answer = -1
        
    return answer
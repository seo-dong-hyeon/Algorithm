from collections import deque

def takeBoxFromBelt(belt, order):
    cnt = 0

    while len(belt) and len(order):
        if belt[-1] == order[0]:
            belt.pop()
            order.popleft()
            cnt += 1
        else:
            break

    return cnt


def solution(order):
    answer = 0

    order = deque(order)
    belt = deque()
    for i in range(1, len(order) + 1):
        if len(order) and i == order[0]:
            order.popleft()
            answer += 1
        else:
            answer += takeBoxFromBelt(belt, order)
            belt.append(i)

    answer += takeBoxFromBelt(belt, order)

    return answer